# -*- encoding: utf-8 -*-

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class GlobalTestOpenAcademySession(TransactionCase):
    '''
    Global Test to openacademy session model.
    Test create session and trigger constraint
    '''

    # Pseudo-constructor methods
    def setUp(self):
        # Define Global Variable to tests methods
        super(GlobalTestOpenAcademySession, self).setUp()
        self.session = self.env['openacademy.session']
        self.partner_vauxoo = self.env.ref('base.res_partner_23')
        self.course_id = self.env.ref('openacademy.course3')
        self.partner_attende = self.env.ref('base.res_partner_5')

    # Generic Methods

    # Test Methods
    def test_05_instructor_is_attendee(self):
        '''
        Check raise: "A session's instructor can't be an attendee"
        '''
        with self.assertRaisesRegexp(
            ValidationError, "A session's instructor can't be an attendee"):
            self.session.create({
                'name': 'Session Test 1',
                'seats': 1,
                'user_id': self.partner_vauxoo.id,
                'attendee_ids': [(6, 0, [self.partner_vauxoo.id])],
                'course_id': self.course_id.id
                })

    def test_10_wkf_done(self):
        '''
        Check that workflow work fine!
        '''
        session_test = self.session.create({
            'name': 'Session Test 2',
            'seats': 2,
            'user_id': self.partner_vauxoo.id,
            'attendee_ids': [(6, 0, [self.partner_attende.id])],
            'course_id': self.course_id.id
            })
        # Check Initial State
        self.assertEqual(session_test.state, 'draft', 'Initial state should '
                        'be in draft')
        # Check next state an check it
        session_test.signal_workflow('button_confirm')
        self.assertEqual(session_test.state, 'confirmed', "Signal Confirm "
                        "don't work")
        # Check next state an check it
        session_test.signal_workflow('button_done')
        self.assertEqual(session_test.state, 'done', "Signal Done don't work")
        # self.env.cr.commit() Only for test data generated for test.
        # Please don't use
