import requests

base_url = "http://127.0.0.1:5000/"


def quiz_sign_in_pass():
    url = base_url + 'auth' + '/signin'

    requests.post


def quiz_load_new_lib_fail():
    url = base_url + 'api/loadnew?lib=gg'

    print(url)

    r = requests.post(url)

    assert(r.status_code==401)
    print(r.status_code)


def quiz_load_new_lib_pass():
    url = base_url + 'api/loadnew?lib=jj'

    print(url)
    r = requests.post(url)
    print(r)


if __name__ == "__main__":
    quiz_load_new_lib_fail()
    quiz_load_new_lib_pass()