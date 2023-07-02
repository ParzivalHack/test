import cmd
import requests
import subprocess
import tempfile

class InterceptingTool(cmd.Cmd):
    intro = "Welcome to Intercepting Tool! Type 'help' for a list of commands."
    prompt = "(Intercepting Tool) "

    intercepted_flows = []

    def default(self, line):
        command, _, args = line.partition(' ')
        if command == 'intercept':
            self.do_intercept(args)
        else:
            print("Unknown command. Type 'help' for a list of commands.")

    def do_intercept(self, line):
        """Intercept a URL and modify the request."""
        url = line.strip()
        if not url:
            print("Invalid URL. Please provide a valid URL.")
            return
        try:
            response = requests.get(url)
            request = response.request
            self.intercepted_flows.append(request)
            print("Request intercepted and added to flows.")
        except requests.exceptions.RequestException as e:
            print(f"Error intercepting request: {e}")

    def do_flows(self, line):
        """List all intercepted flows."""
        if not self.intercepted_flows:
            print("No intercepted flows.")
        else:
            for index, flow in enumerate(self.intercepted_flows, start=1):
                print(f"{index}. {flow.url}")

    def do_modify(self, line):
        """Modify an intercepted flow."""
        try:
            flow_index = int(line.strip())
            if flow_index < 1 or flow_index > len(self.intercepted_flows):
                print("Invalid flow index.")
            else:
                flow = self.intercepted_flows[flow_index - 1]
                modified_request = self.edit_request(flow)
                if modified_request:
                    # Send the modified request
                    try:
                        session = requests.Session()
                        response = session.send(modified_request)
                        print("Modified request sent successfully.")
                    except requests.exceptions.RequestException as e:
                        print(f"Error sending modified request: {e}")
        except ValueError:
            print("Invalid flow index.")

    def edit_request(self, flow):
        """Edit the intercepted request using an external text editor."""
        with tempfile.NamedTemporaryFile(suffix=".http") as temp_file:
            temp_file.write(f"{flow.method} {flow.url}\n".encode())
            for header, value in flow.headers.items():
                temp_file.write(f"{header}: {value}\n".encode())
            temp_file.write(b"\n")
            if flow.body:
                temp_file.write(flow.body)
            temp_file.flush()
            try:
                subprocess.call(["nano", temp_file.name])
                temp_file.seek(0)
                modified_request_text = temp_file.read().decode()
                modified_request = requests.Request()
                modified_request.prepare(
                    method=flow.method,
                    url=flow.url,
                    headers=flow.headers,
                    data=modified_request_text if modified_request_text else flow.body,
                )
                return modified_request
            except FileNotFoundError:
                print("Error: nano text editor not found.")
            except subprocess.CalledProcessError:
                print("Error: Failed to open text editor.")
        return None

    def do_quit(self, line):
        """Exit the intercepting tool."""
        print("Exiting intercepting tool.")
        return True

    def emptyline(self):
        pass

if __name__ == "__main__":
    InterceptingTool().cmdloop()
