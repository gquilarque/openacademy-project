# -*- encoding: utf-8 -*-

from psycopg2 import IntegrityError

from openerp.tests.common import TransactionCase
from openerp.tools import mute_logger

class GlobalTestOpenAcademyCourse(TransactionCase):
    '''
    Global Test to openacademy course model.
    Test create course and trigger constraint
    '''

    def setUp(self):
        # Define Global Variable to tests methods
        super(GlobalTestOpenAcademyCourse,self).setUp()
        self.course = self.env['openacademy.course']

    # Class's Method that is not test
    def create_course(self, course_name, course_description,course_user_id):
        # Create a course with the parameters received
        course_id = self.course.create({
            'name': course_name,
            'description': course_description,
            'user_id':course_user_id,
            })
        return course_id

    # Test Method start with 'def test_*(self)'
    # Mute Error openerp.sql_db to avoid it in log
    @mute_logger('openerp.sql_db') 
    def test_01_same_name_description(self):
        '''
        Test create a course with same name and description
        to test constraint of name and description are different.
        '''
        # Error Raised Expected with Message Expected
        with self.assertRaisesRegexp(
            IntegrityError,
            'new row for relation "openacademy_course" violates '
            'check constraint "openacademy_course_name_description_check"'):
            # Create a course with same name and description to raise error
            self.create_course('test','test',None)
        
