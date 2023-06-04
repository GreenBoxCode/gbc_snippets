import re
import datetime


class InputSanitizer:
    """Sanitize user input to prevent code injection attacks.
    This class is intended to be used in a web application.
    Instantiate the class and call the sanitize_input() method.
    The method will return the string if it passes the sanitization.
    If the string fails the sanitization, the method will return a
    string indicating the error and log the incident to a file
    named input_sanitizer.log
    Example usage:
    sanitizer = InputSanitizer()
    user_input = input("Enter your input: ")
    sanitized_input = sanitizer.sanitize_input(user_input)
    print(f"Sanitized input: {sanitized_input}")

    The sanitize_input() method uses the re module to remove any
    characters that are not alphanumeric, comma, period, or space.
    """

    def sanitize_input(self, user_input):
        try:
            sanitized_input = re.sub(r"[^a-zA-Z0-9., ]", "", user_input)
            # test the input to see if it is empty
            if sanitized_input == "":
                raise ValueError("Input is empty.")
            # test the input to see if it contains invalid characters
            if sanitized_input != user_input:
                raise ValueError("Input contains invalid characters.")
            return sanitized_input
        except Exception as e:
            print(f"Error sanitizing input: {str(e)}")
            with open("input_sanitizer.log", "a") as log_file:
                datetime_string = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                log_file.write(
                    f"[{datetime_string}] Error sanitizing input: {str(e)}\n"
                    f'Input: "{user_input}"\n'
                )
            return "Input Error: Invalid characters detected. The incident has been logged."


# Example usage
if __name__ == "__main__":
    sanitizer = InputSanitizer()
    user_input = input("Enter your input: ")
    sanitized_input = sanitizer.sanitize_input(user_input)
    print(f"Sanitized input: {sanitized_input}")
