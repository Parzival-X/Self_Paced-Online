#!/usr/bin/env python3
"""Unit tests for HTML Render"""
import os
import unittest
import html_render as hr


class TestHtmlRender(unittest.TestCase):
    """Test class containing all unit tests for the Element class"""
    def setUp(self):
        self.html = hr.HtmlElement()
        self.head = hr.HeadElement(hr.TitleElement('This is a title'))
        self.body = hr.BodyElement()
        self.para = hr.ParagraphElement(500, style='Bold', cls='Intro')
        self.horz = hr.HrElement()

    def tearDown(self):
        # Remove any unit test generated files
        files = os.listdir()
        for f in files:
            if "unit_test_" in f:
                os.remove(os.path.join(os.getcwd(), f))

    def test_append(self):
        """Test the append method"""
        self.html.append('Testing the append method...')
        self.assertTrue(self.html.content == [
                        'Testing the append method...'],
                        msg=self.html.content)

    def test_render_def_indent(self):
        """Test the render method with def indentation"""
        self.html.append('Testing the render method...')
        answer = ('<html>\n'
                  '    Testing the render method...\n'
                  '</html>\n')

        with open('unit_test_render.txt', 'w+') as f:
            self.html.render(f)
            f.seek(0)
            result = f.read(50)
            self.assertTrue(result == answer, msg=result)

    def test_render_custom_indent(self):
        """Test the render method with custom indentation"""
        self.html.append('Testing the render method...')
        answer = ('    <html>\n'
                  '        Testing the render method...\n'
                  '    </html>\n')

        with open('unit_test_render.txt', 'w+') as f:
            self.html.render(f, '    ')
            f.seek(0)
            result = f.read(60)
            self.assertTrue(result == answer, msg=result)

    def test_render_nested(self):
        """Test the render method with nested elements"""
        self.body.append(hr.ParagraphElement(500))
        self.html.append(self.head)
        self.html.append(self.body)
        answer = ('<html>\n'
                  '    <head>\n'
                  '        <title> This is a title </title>\n'
                  '    </head>\n'
                  '    <body>\n'
                  '        <p>\n'
                  '            500\n'
                  '        </p>\n'
                  '    </body>\n'
                  '</html>\n')

        with open('unit_test_render.txt', 'w+') as f:
            self.html.render(f)
            f.seek(0)
            result = f.read(200)
            self.assertTrue(result == answer, msg=result)

    def test_render_nested_with_attrs(self):
        """Test the render method with nested elements"""
        self.body.append(self.para)
        self.html.append(self.head)
        self.html.append(self.body)
        answer = ('<html>\n'
                  '    <head>\n'
                  '        <title> This is a title </title>\n'
                  '    </head>\n'
                  '    <body>\n'
                  '        <p style="Bold" cls="Intro">\n'
                  '            500\n'
                  '        </p>\n'
                  '    </body>\n'
                  '</html>\n')

        with open('unit_test_render.txt', 'w+') as f:
            self.html.render(f)
            f.seek(0)
            result = f.read(200)
            self.assertTrue(result == answer, msg=result)

    def test_render_self_closing(self):
        """Test the render method with self closing elements"""
        self.body.append(self.para)
        self.body.append(self.horz)
        self.html.append(self.head)
        self.html.append(self.body)
        answer = ('<html>\n'
                  '    <head>\n'
                  '        <title> This is a title </title>\n'
                  '    </head>\n'
                  '    <body>\n'
                  '        <p style="Bold" cls="Intro">\n'
                  '            500\n'
                  '        </p>\n'
                  '        <hr />\n'
                  '    </body>\n'
                  '</html>\n')

        with open('unit_test_render.txt', 'w+') as f:
            self.html.render(f)
            f.seek(0)
            result = f.read(250)
            self.assertTrue(result == answer, msg=result)

    def test_render_self_closing_with_content(self):
        """Test the render method with self closing elements and attempt
           to manipulate the content attribute
        """
        self.body.append(self.para)
        self.body.append(self.horz)
        self.html.append(self.head)
        self.html.append(self.body)
        self.horz.content = ['Attempt to adjust content']
        answer = ('<html>\n'
                  '    <head>\n'
                  '        <title> This is a title </title>\n'
                  '    </head>\n'
                  '    <body>\n'
                  '        <p style="Bold" cls="Intro">\n'
                  '            500\n'
                  '        </p>\n'
                  '        <hr />\n'
                  '    </body>\n'
                  '</html>\n')

        with open('unit_test_render.txt', 'w+') as f:
            self.html.render(f)
            f.seek(0)
            result = f.read(250)
            self.assertTrue(result == answer, msg=result)


if __name__ == '__main__':
    unittest.main()
