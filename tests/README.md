![CrowdStrike Falcon](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# FalconPy Unit Testing
The contents of this folder are used to unit test the FalconPy code base.
Developers who are wanting to contribute to the FalconPy project can review this documentation for
detail regarding how to unit test successfully so that pull request submissions are not delayed.

+ [Available tests](#available-tests)
+ [Configuring your environment](#configuring-your-environment)
+ [Running a single unit test](#running-a-single-unit-test)
+ [Executing the entire unit test series](#executing-the-entire-unit-test-series)
+ [Checking code and docstring style](#checking-code-and-docstring-style)
+ [Questions](#questions)

## Available tests
A unit test is available for every Service Class implemented within FalconPy and are named after the Service Class module being tested.

There are also a few additional files and unit tests within this directory that are used as part of other unit tests, or to test certain library aspects to complete code coverage.
| File name | Purpose |
| :--- | :-- |
| `conftest.py` | Pytest configuration file. Ignored. |
| `coverage.svg` | Generated coverage badge. |
| `test_authentications.py` | Tests authentication functionality and creates the authentication object used by all other unit tests. |
| `test_authorization.py` | Authorization, Service vs. Uber authentication and cross-cloud authentication testing. |
| `test_timeout.py` | Tests timeout handling functionality. |
| `test_uber_api_complete.py` | Tests the Uber Class. |
| `testfile.png` | Test file used for upload & download testing within the API. |


## Configuring your environment
In order to run unit testing successfully, you will need to configure your environment.

### Development requirements
The necessary Python requirements for development and testing can be found in `requirements-dev.txt`.
Install these requirements with the following command:

```shell
pip3 install -r requirements-dev.txt
```

### Environment variables
There are two required environment variables, and three optional environment variables used for unit testing. Set these before starting your test series.

#### Example

```shell
export DEBUG_API_ID=CROWDSTRIKE-API-ID-GOES-HERE
```

| Variable name | Purpose | Required |
| :--- | :--- | :--- |
| `DEBUG_API_ID` | Contains the CrowdStrike Falcon API client ID used for testing. | ![Yes](https://img.shields.io/badge/-YES-darkgreen?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAOCAYAAAAi2ky3AAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TpaIVBzuIOGSoDmJBVEQ3rUIRKoRaoVUHk5f+CE0akhQXR8G14ODPYtXBxVlXB1dBEPwBcXNzUnSREu9LCi1ifPB4H+e9c7jvXkColZhmtY0Cmm6bqURczGRXxNAruhAEMI1hmVnGrCQl4bu+7hHg512MZ/m/+3N1qzmLAQGReIYZpk28Tjy5aRuc94kjrCirxOfEIyYVSPzIdcXjN84FlwWeGTHTqTniCLFYaGGlhVnR1IgniKOqplO+kPFY5bzFWStVWKNO/sNwTl9e4jrtASSwgEVIEKGggg2UYCNGp06KhRTdx338/a5fIpdCrg0wcsyjDA2y6wefwe/eWvnxMS8pHAfaXxznYxAI7QL1quN8HztO/QQIPgNXetNfrgFTn6RXm1r0COjZBi6um5qyB1zuAH1PhmzKrsTnL+TzwPsZjSkL9N4Cnate3xr3OH0A0tSr5A1wcAgMFSh7zeffHa19+/dNo38/hq9yr+iELI0AAAAGYktHRAAAAAAAAPlDu38AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQflDAsTByz7Va2cAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAYBJREFUKM+lkjFIlVEYht/zn3sFkYYUyUnIRcemhCtCU6JQOLiIU+QeJEQg6BBIm0s4RBCBLjq5OEvgJC1uOniJhivesLx17/97/vO9b4NK4g25157hfHCGB773/cA0HZIEAKiMj+LWiOxljG/i96pnCFP58XHnrWX2+9cj0dYl9Yu2FE9/9rXrcAAgs2eSyiBfOe/XRD503h/CuffOubQVUXL+Jh9BllzBbyJJBgDclVkO4Kukd8zzkXJbeUljIldFTstsmSHM6S81ma2KfPKlFdkGAMY4wzx/bbXapMy21My+YizdKNq5mDzLkrxafSxySFKjSWX2oTmjKzz4vN0r2lOFcL/Q3V0/mX95ILMXTTGYVfaut/aP2+oCMAvnZgCcsF5fcR0dg65YHAdwB+QApADvu0AuOe/ftlJAD7Nsgmm6yBjDtfWORJZlNtFyo/lR5Z7MyheKA5ktSur7sTAHazSG27pehjAiaVfkN8b4XFIJ/wOzbOx07VNRUuHy7w98CzCcGPyWywAAAABJRU5ErkJggg==) |
| `DEBUG_API_SECRET` | Contains the CrowdStrike Falcon API client secret used for testing. | ![Yes](https://img.shields.io/badge/-YES-darkgreen?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAOCAYAAAAi2ky3AAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TpaIVBzuIOGSoDmJBVEQ3rUIRKoRaoVUHk5f+CE0akhQXR8G14ODPYtXBxVlXB1dBEPwBcXNzUnSREu9LCi1ifPB4H+e9c7jvXkColZhmtY0Cmm6bqURczGRXxNAruhAEMI1hmVnGrCQl4bu+7hHg512MZ/m/+3N1qzmLAQGReIYZpk28Tjy5aRuc94kjrCirxOfEIyYVSPzIdcXjN84FlwWeGTHTqTniCLFYaGGlhVnR1IgniKOqplO+kPFY5bzFWStVWKNO/sNwTl9e4jrtASSwgEVIEKGggg2UYCNGp06KhRTdx338/a5fIpdCrg0wcsyjDA2y6wefwe/eWvnxMS8pHAfaXxznYxAI7QL1quN8HztO/QQIPgNXetNfrgFTn6RXm1r0COjZBi6um5qyB1zuAH1PhmzKrsTnL+TzwPsZjSkL9N4Cnate3xr3OH0A0tSr5A1wcAgMFSh7zeffHa19+/dNo38/hq9yr+iELI0AAAAGYktHRAAAAAAAAPlDu38AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQflDAsTByz7Va2cAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAYBJREFUKM+lkjFIlVEYht/zn3sFkYYUyUnIRcemhCtCU6JQOLiIU+QeJEQg6BBIm0s4RBCBLjq5OEvgJC1uOniJhivesLx17/97/vO9b4NK4g25157hfHCGB773/cA0HZIEAKiMj+LWiOxljG/i96pnCFP58XHnrWX2+9cj0dYl9Yu2FE9/9rXrcAAgs2eSyiBfOe/XRD503h/CuffOubQVUXL+Jh9BllzBbyJJBgDclVkO4Kukd8zzkXJbeUljIldFTstsmSHM6S81ma2KfPKlFdkGAMY4wzx/bbXapMy21My+YizdKNq5mDzLkrxafSxySFKjSWX2oTmjKzz4vN0r2lOFcL/Q3V0/mX95ILMXTTGYVfaut/aP2+oCMAvnZgCcsF5fcR0dg65YHAdwB+QApADvu0AuOe/ftlJAD7Nsgmm6yBjDtfWORJZlNtFyo/lR5Z7MyheKA5ktSur7sTAHazSG27pehjAiaVfkN8b4XFIJ/wOzbOx07VNRUuHy7w98CzCcGPyWywAAAABJRU5ErkJggg==) |
| `DEBUG_API_BASE_URL` | Contains the CrowdStrike [base URL]() used for requests to the API. Only required for unit testing in the CrowdStrike **US-GOV-1** region. Specify `usgov1` if you are testing in this region. | ![No](https://img.shields.io/badge/-NO-maroon?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAOCAYAAAAi2ky3AAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TpaIVBzuIOGSoDmJBVEQ3rUIRKoRaoVUHk5f+CE0akhQXR8G14ODPYtXBxVlXB1dBEPwBcXNzUnSREu9LCi1ifPB4H+e9c7jvXkColZhmtY0Cmm6bqURczGRXxNAruhAEMI1hmVnGrCQl4bu+7hHg512MZ/m/+3N1qzmLAQGReIYZpk28Tjy5aRuc94kjrCirxOfEIyYVSPzIdcXjN84FlwWeGTHTqTniCLFYaGGlhVnR1IgniKOqplO+kPFY5bzFWStVWKNO/sNwTl9e4jrtASSwgEVIEKGggg2UYCNGp06KhRTdx338/a5fIpdCrg0wcsyjDA2y6wefwe/eWvnxMS8pHAfaXxznYxAI7QL1quN8HztO/QQIPgNXetNfrgFTn6RXm1r0COjZBi6um5qyB1zuAH1PhmzKrsTnL+TzwPsZjSkL9N4Cnate3xr3OH0A0tSr5A1wcAgMFSh7zeffHa19+/dNo38/hq9yr+iELI0AAAAGYktHRAAAAAAAAPlDu38AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQflDAsTByz7Va2cAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAYBJREFUKM+lkjFIlVEYht/zn3sFkYYUyUnIRcemhCtCU6JQOLiIU+QeJEQg6BBIm0s4RBCBLjq5OEvgJC1uOniJhivesLx17/97/vO9b4NK4g25157hfHCGB773/cA0HZIEAKiMj+LWiOxljG/i96pnCFP58XHnrWX2+9cj0dYl9Yu2FE9/9rXrcAAgs2eSyiBfOe/XRD503h/CuffOubQVUXL+Jh9BllzBbyJJBgDclVkO4Kukd8zzkXJbeUljIldFTstsmSHM6S81ma2KfPKlFdkGAMY4wzx/bbXapMy21My+YizdKNq5mDzLkrxafSxySFKjSWX2oTmjKzz4vN0r2lOFcL/Q3V0/mX95ILMXTTGYVfaut/aP2+oCMAvnZgCcsF5fcR0dg65YHAdwB+QApADvu0AuOe/ftlJAD7Nsgmm6yBjDtfWORJZlNtFyo/lR5Z7MyheKA5ktSur7sTAHazSG27pehjAiaVfkN8b4XFIJ/wOzbOx07VNRUuHy7w98CzCcGPyWywAAAABJRU5ErkJggg==) |
| `CROSS_DEBUG_KEY` | Used to test cross cloud authentication. Contains a CrowdStrike API client ID. Can be left null, or set to the same value as `DEBUG_API_ID` | ![No](https://img.shields.io/badge/-NO-maroon?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAOCAYAAAAi2ky3AAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TpaIVBzuIOGSoDmJBVEQ3rUIRKoRaoVUHk5f+CE0akhQXR8G14ODPYtXBxVlXB1dBEPwBcXNzUnSREu9LCi1ifPB4H+e9c7jvXkColZhmtY0Cmm6bqURczGRXxNAruhAEMI1hmVnGrCQl4bu+7hHg512MZ/m/+3N1qzmLAQGReIYZpk28Tjy5aRuc94kjrCirxOfEIyYVSPzIdcXjN84FlwWeGTHTqTniCLFYaGGlhVnR1IgniKOqplO+kPFY5bzFWStVWKNO/sNwTl9e4jrtASSwgEVIEKGggg2UYCNGp06KhRTdx338/a5fIpdCrg0wcsyjDA2y6wefwe/eWvnxMS8pHAfaXxznYxAI7QL1quN8HztO/QQIPgNXetNfrgFTn6RXm1r0COjZBi6um5qyB1zuAH1PhmzKrsTnL+TzwPsZjSkL9N4Cnate3xr3OH0A0tSr5A1wcAgMFSh7zeffHa19+/dNo38/hq9yr+iELI0AAAAGYktHRAAAAAAAAPlDu38AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQflDAsTByz7Va2cAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAYBJREFUKM+lkjFIlVEYht/zn3sFkYYUyUnIRcemhCtCU6JQOLiIU+QeJEQg6BBIm0s4RBCBLjq5OEvgJC1uOniJhivesLx17/97/vO9b4NK4g25157hfHCGB773/cA0HZIEAKiMj+LWiOxljG/i96pnCFP58XHnrWX2+9cj0dYl9Yu2FE9/9rXrcAAgs2eSyiBfOe/XRD503h/CuffOubQVUXL+Jh9BllzBbyJJBgDclVkO4Kukd8zzkXJbeUljIldFTstsmSHM6S81ma2KfPKlFdkGAMY4wzx/bbXapMy21My+YizdKNq5mDzLkrxafSxySFKjSWX2oTmjKzz4vN0r2lOFcL/Q3V0/mX95ILMXTTGYVfaut/aP2+oCMAvnZgCcsF5fcR0dg65YHAdwB+QApADvu0AuOe/ftlJAD7Nsgmm6yBjDtfWORJZlNtFyo/lR5Z7MyheKA5ktSur7sTAHazSG27pehjAiaVfkN8b4XFIJ/wOzbOx07VNRUuHy7w98CzCcGPyWywAAAABJRU5ErkJggg==) |
| `CROSS_DEBUG_SECRET` | Used to test cross cloud authentication. Contains a CrowdStrike API client secret. Can be left null, or set to the same value as `DEBUG_API_SECRET` | ![No](https://img.shields.io/badge/-NO-maroon?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAAOCAYAAAAi2ky3AAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TpaIVBzuIOGSoDmJBVEQ3rUIRKoRaoVUHk5f+CE0akhQXR8G14ODPYtXBxVlXB1dBEPwBcXNzUnSREu9LCi1ifPB4H+e9c7jvXkColZhmtY0Cmm6bqURczGRXxNAruhAEMI1hmVnGrCQl4bu+7hHg512MZ/m/+3N1qzmLAQGReIYZpk28Tjy5aRuc94kjrCirxOfEIyYVSPzIdcXjN84FlwWeGTHTqTniCLFYaGGlhVnR1IgniKOqplO+kPFY5bzFWStVWKNO/sNwTl9e4jrtASSwgEVIEKGggg2UYCNGp06KhRTdx338/a5fIpdCrg0wcsyjDA2y6wefwe/eWvnxMS8pHAfaXxznYxAI7QL1quN8HztO/QQIPgNXetNfrgFTn6RXm1r0COjZBi6um5qyB1zuAH1PhmzKrsTnL+TzwPsZjSkL9N4Cnate3xr3OH0A0tSr5A1wcAgMFSh7zeffHa19+/dNo38/hq9yr+iELI0AAAAGYktHRAAAAAAAAPlDu38AAAAJcEhZcwAACxMAAAsTAQCanBgAAAAHdElNRQflDAsTByz7Va2cAAAAGXRFWHRDb21tZW50AENyZWF0ZWQgd2l0aCBHSU1QV4EOFwAAAYBJREFUKM+lkjFIlVEYht/zn3sFkYYUyUnIRcemhCtCU6JQOLiIU+QeJEQg6BBIm0s4RBCBLjq5OEvgJC1uOniJhivesLx17/97/vO9b4NK4g25157hfHCGB773/cA0HZIEAKiMj+LWiOxljG/i96pnCFP58XHnrWX2+9cj0dYl9Yu2FE9/9rXrcAAgs2eSyiBfOe/XRD503h/CuffOubQVUXL+Jh9BllzBbyJJBgDclVkO4Kukd8zzkXJbeUljIldFTstsmSHM6S81ma2KfPKlFdkGAMY4wzx/bbXapMy21My+YizdKNq5mDzLkrxafSxySFKjSWX2oTmjKzz4vN0r2lOFcL/Q3V0/mX95ILMXTTGYVfaut/aP2+oCMAvnZgCcsF5fcR0dg65YHAdwB+QApADvu0AuOe/ftlJAD7Nsgmm6yBjDtfWORJZlNtFyo/lR5Z7MyheKA5ktSur7sTAHazSG27pehjAiaVfkN8b4XFIJ/wOzbOx07VNRUuHy7w98CzCcGPyWywAAAABJRU5ErkJggg==) |

### API Scopes
Unit test series are designed to test every code path within every module of the library, meaning every method of every class. A single unit test series is over 200 individual unit tests, many of which make multiple requests to the CrowdStrike Falcon API. In order for unit tests to be successful, they will need API credentials scoped to allow them permissions to execute the operations they are performing. (Although many unit tests will accept credential failure as an allowed result.)

Developers should either limit their local unit testing to API service collections they are focused on, leveraging API credentials scoped to these collections, or use a development key that is scoped to all of the API service collections being tested.

> An API credential scoped to every CrowdStrike API service collection is an _extremely powerful_ token. This credential should be guarded closely with the secret rotated on a regular basis.

## Running a single unit test
A single unit test can be executed using the `unit-test.sh` utility within the `util` folder.

From the main folder execute the following command where {unit_test_name} is the name of the service collection you are testing:

```shell
util/unit-test.sh {unit_test_name}
```

#### Example
For an example, let's run a unit test of the source of the Detects Service Class.

```shell
util/unit-test.sh detects
```

#### Result
Our test runs and results are provided immediately as they are produced.

```shell
============================================================= test session starts =============================================================
platform darwin -- Python 3.9.9, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- /usr/local/opt/python@3.9/bin/python3.9
cachedir: .pytest_cache
rootdir: /Users/jhiller/Desktop/Code/falconpy-ver_1.0.0
collected 7 items

tests/test_detects.py::TestDetects::test_query_detects PASSED
tests/test_detects.py::TestDetects::test_get_detect_summaries PASSED
tests/test_detects.py::TestDetects::test_all_functionality PASSED
tests/test_detects.py::TestDetects::test_validation_failure PASSED
tests/test_detects.py::TestDetects::test_validation_datatype_failure PASSED
tests/test_detects.py::TestDetects::test_validation_invalid_param_failure PASSED
tests/test_detects.py::TestDetects::test_validation_disable PASSED

============================================================== 7 passed in 6.95s ==============================================================
```

Once the test completes, you are provided coverage results. Note how in this example, the Detects Service Class has 100% coverage.
Since we are only testing the one Service Class in this example our coverage miss in the other Service Classes is expected.

For private modules such as the `_endpoint` or `_payload` submodules, or files such as `__init__.py` or `_result.py`, etc. coverage results should be ignore when performing
singular unit testing.

```shell
Name                                                             Stmts   Miss  Cover
------------------------------------------------------------------------------------
src/falconpy/__init__.py                                            62      0   100%
src/falconpy/_base_url.py                                            7      0   100%
src/falconpy/_endpoint/__init__.py                                 117      0   100%
... trimmed for brevity

src/falconpy/_payload/__init__.py                                   24      0   100%
... trimmed for brevity

src/falconpy/_result.py                                              8      0   100%
src/falconpy/_service_class.py                                      73     38    48%
src/falconpy/_util.py                                              181     44    76%
src/falconpy/_version.py                                            10      0   100%
src/falconpy/api_complete.py                                       111     97    13%
src/falconpy/cloud_connect_aws.py                                   47     15    68%
src/falconpy/cspm_registration.py                                  114     47    59%
src/falconpy/custom_ioa.py                                          85     31    64%
src/falconpy/d4c_registration.py                                    47     17    64%
src/falconpy/detects.py                                             28      0   100%
src/falconpy/device_control_policies.py                             66     29    56%
src/falconpy/discover.py                                            10      2    80%
src/falconpy/event_streams.py                                       19      8    58%
src/falconpy/falcon_complete_dashboard.py                           76     28    63%
... trimmed for brevity

src/falconpy/user_management.py                                     69     30    57%
src/falconpy/zero_trust_assessment.py                               12      2    83%
------------------------------------------------------------------------------------
TOTAL                                                             3650   1573    57%
```

## Executing the entire unit test series
The entire unit testing series can be run using the `run-tests.sh` utility within the `util` folder.

From the main folder execute the following command:

```shell
util/run-tests.sh
```

Unit tests will be collected and then begin to execute in order.

```shell
============================================================= test session starts =============================================================
platform darwin -- Python 3.9.9, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- /usr/local/opt/python@3.9/bin/python3.9
cachedir: .pytest_cache
rootdir: /Users/jhiller/Desktop/Code/falconpy-ver_1.0.0
collected 209 items

tests/test_authentications.py::TestAuthentications::test_BadCredentialAuth PASSED
tests/test_authentications.py::TestAuthentications::test_BadCredRevoke PASSED
tests/test_authentications.py::TestAuthentications::test_StaleObjectAuth PASSED
tests/test_authentications.py::TestAuthentications::test_BadObjectAuth PASSED
tests/test_authentications.py::TestAuthentications::test_badBaseURL PASSED
tests/test_authentications.py::TestAuthentications::test_crossCloudFailure PASSED
tests/test_authentications.py::TestAuthentications::test_checkRegionLookups PASSED
tests/test_authentications.py::TestAuthentications::test_crossGovCloudSelectFailure PASSED
tests/test_authentications.py::TestAuthentications::test_ObjectAuth PASSED
tests/test_authorization.py::TestAuthorization::test_uberAuth PASSED
tests/test_authorization.py::TestAuthorization::test_uberRevoke PASSED
tests/test_authorization.py::TestAuthorization::test_serviceAuth PASSED
tests/test_authorization.py::TestAuthorization::test_serviceAuthNoSSL PASSED
tests/test_authorization.py::TestAuthorization::test_serviceMSSPAuth PASSED
tests/test_authorization.py::TestAuthorization::test_uberMSSPAuthFailure PASSED
tests/test_authorization.py::TestAuthorization::test_serviceRevoke PASSED
tests/test_authorization.py::TestAuthorization::test_failServiceAuth PASSED
tests/test_authorization.py::TestAuthorization::test_base_url_lookup PASSED
tests/test_authorization.py::TestAuthorization::test_fail_base_url_lookup PASSED
tests/test_cloud_connect_aws.py::TestCloudConnectAWS::test_GetAWSSettings PASSED
tests/test_cloud_connect_aws.py::TestCloudConnectAWS::test_QueryAWSAccounts PASSED
tests/test_cloud_connect_aws.py::TestCloudConnectAWS::test_GetAWSAccounts PASSED
tests/test_cloud_connect_aws.py::TestCloudConnectAWS::test_GetAWSAccountsUsingList PASSED
tests/test_cloud_connect_aws.py::TestCloudConnectAWS::test_QueryAWSAccountsForIDs PASSED
... trimmed for brevity
```

When finished, testing results are displayed immediately before coverage is calculated.

```shell
======================================================= 209 passed in 429.00s (0:07:09) =======================================================
```

Then coverage is displayed.

```shell
Name                                                             Stmts   Miss  Cover
------------------------------------------------------------------------------------
src/falconpy/__init__.py                                            62      0   100%
src/falconpy/_base_url.py                                            7      0   100%
src/falconpy/_endpoint/__init__.py                                 117      0   100%
... trimmed for brevity

src/falconpy/sensor_download.py                                     32      0   100%
src/falconpy/sensor_update_policy.py                                99      0   100%
src/falconpy/sensor_visibility_exclusions.py                        32      0   100%
src/falconpy/spotlight_vulnerabilities.py                           25      0   100%
src/falconpy/user_management.py                                     69      0   100%
src/falconpy/zero_trust_assessment.py                               12      0   100%
------------------------------------------------------------------------------------
TOTAL                                                             3650      0   100%
```

Finally, a bandit static code analysis is performed.

```shell
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.9.9
134 [0.. 50.. 100.. ]
Run started:2022-01-30 05:08:59.847937

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 33978
	Total lines skipped (#nosec): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0.0
		Low: 0.0
		Medium: 0.0
		High: 0.0
	Total issues (by confidence):
		Undefined: 0.0
		Low: 0.0
		Medium: 0.0
		High: 0.0
Files skipped (0):
```

## Checking code and docstring style
Two helper utilities are provided to assist you with confirming code quality and style.

`lint.sh` will lint the entire package.

#### Example

```shell
util/lint.sh
```

#### Result

```shell
0

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

`docstyle.sh` will check the formatting of docstrings within the source of the package.

#### Example

```shell
util/docstyle.sh
```

#### Result

```shell
0
```

## Questions
Having trouble getting unit testing to perform the way you expect?  [Let us know](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AQ%26A), we're happy to assist.

[![Discussions](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/ask-a-question.png)](https://github.com/CrowdStrike/falconpy/discussions?discussions_q=category%3AQ%26A)

---

<p align="center"><img src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-footer.png"><BR/><img width="300px" src="https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/adversary-bear-2.png"></P>
<h3><P align="center">WE STOP BREACHES</P></h3>
