from behave import given, use_step_matcher

use_step_matcher("re")

@given(u'I navigate to the kayak main page')
def visit_login(context):
    context.browser.get("https://www.kayak.com.co")
