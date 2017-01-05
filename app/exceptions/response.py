from flask import make_response, jsonify, abort, current_app
from werkzeug.http import HTTP_STATUS_CODES
import sys, os, traceback

"""
Helper to make API returns more consistent
"""


def make_json_response(response, code=200):
    # If response type is not defined, use default HTTP status
    if code is not 200 and not response['errors']['type']:
        response['errors']['type'] = HTTP_STATUS_CODES['code']

    return make_response(jsonify(response), code)


def make_success_resp(msg=None):
    response = {
        'success': True,
        'message': msg or ''
    }
    return make_json_response(response)


def make_data_resp(data, msg=None):
    response = {
        'success': True,
        'data': data,
        'message': msg or ''
    }
    return make_json_response(response)


def make_error_resp(msg, err_type=None, code=400):
    response = {
        'errors': {
            'message': msg or "Something is horribly wrong!",
            'type': err_type,
            'more info': ''
        }
    }
    return make_json_response(response, code)


def make_form_error_resp(form, msg=None):
    err_type = 'Form validation error.'
    if not msg:
        msg = form.errors
    return make_error_resp(msg=msg, err_type=err_type, code=422)


def make_exception_resp(exception, err_type=None, code=500):
    # Do not display the exception to users in production
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    # include filename, line number and stacktrace
    msg = "Exception: %s: %s: %s: %s:" % (exc_type, fname, exc_tb.tb_lineno, traceback.format_exc())
    current_app.logger.critical('Exception caught: %s' % msg)
    return make_error_resp(msg="Internal server error. Report this problem!", err_type=err_type, code=422)