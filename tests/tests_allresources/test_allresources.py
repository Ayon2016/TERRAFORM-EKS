from conftest import actual_output, expected_output  # Import the fixtures from conftest
import pytest

class TestAllResourcesinPlanOutput:

    exception_info = []  # Store caught exception info

    @pytest.mark.usefixtures("actual_output", "expected_output")
    def test_that_all_resourcesfromplanout_exist(self, actual_output, expected_output):   
        try:
            for key, value in expected_output.items():
                if "subnet" in key or "aws_launch_template" in key:
                    print("these are region specific values that'll change with a cluster deployment in another region")
                    for key1, value1 in actual_output.items():
                        if "subnet" in key1 or "aws_launch_template" in key1:
                            print("Printing the keys for your reference - " + str(key1))
                else:
                    assert value in actual_output
        except AssertionError as e:
            print("Assertion error:", e)
            self.exception_info.append(str(e))
            raise e
        except Exception as e:
            print("An error occurred:", e)
            self.exception_info.append(str(e))
            raise e