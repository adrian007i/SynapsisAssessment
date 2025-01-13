import os, shutil
from Helper import format_print, valid_folder_name

ROOT = os.path.abspath("..")

os.system("cls")


class Alert:
    """
    Checks a list of sunapsis alerts and move custom alerts into a the university alerts directory.
    """

    def __init__(self, working_dir: str, university_name: str):
        """
        :param working_dir: working directory name where file manipulation will take place
        :param university_name: Name of University
        """

        self.working_dir = working_dir
        self.university_name = university_name
        self.system_list = set()

    def directory_setup(self, synapsis_dir: str) -> dict:
        """
        Create the necessary folders and initialize the working directory
        :param synapsis_dir: original synapsis root directory
        :return: dictionary of success and any error messages
        """

        os.chdir(ROOT)

        if not os.path.isdir(synapsis_dir):
            return {"success": False, "msg": f"Invalid Directory '{synapsis_dir}'"}

        if not valid_folder_name(self.university_name):
            return {
                "success": False,
                "msg": f"Invalid folder name: {self.university_name}",
            }

        if os.path.exists(self.working_dir):
            shutil.rmtree(self.working_dir)

        shutil.copytree(synapsis_dir, self.working_dir)
        os.makedirs(os.path.join(self.working_dir, self.university_name, "alerts"))

        return {"success": True, "msg": "Directory Setup Complete"}

    def load_system_list(self, system_list_file: str) -> dict:
        """
        Loads the contents from the "systemList.txt" file into memory "HashSet"
        :param str system_list_file: txt file that contains all system alerts
        :return: dictionary of success and any error messages
        """

        os.chdir(os.path.join(ROOT, self.working_dir))

        try:
            with open(system_list_file, "r") as file:
                for line in file:
                    self.system_list.add(line.strip())

            return {"success": True, "msg": f"System List Loaded"}

        except FileNotFoundError:
            return {"success": False, "msg": f"{system_list_file} was not found"}
        except PermissionError:
            return {"success": False, "msg": f"Access denied to {system_list_file}"}
        except Exception as e:
            return {"success": False, "msg": str(e)}

    def move_custom_alerts(self) -> dict:
        """
        Checks if the alert is custom and move it into the "/University/Alerts" directory
        :return: dictionary of success and any error messages
        """
        os.chdir(os.path.join(ROOT, self.working_dir))

        alerts_dir = os.path.join("ioffice", "alerts")

        try:
            custom_alerts = 0

            # iterate all files in the alerts directory
            for file in os.listdir(alerts_dir):

                # check if the file exist in the system_list hashset
                if file not in self.system_list:

                    custom_alerts += 1

                    shutil.move(
                        os.path.join(alerts_dir, file),
                        os.path.join(self.university_name, "alerts", file),
                    )

            return {
                "success": True,
                "msg": f"Successfully Moved {custom_alerts} Alerts",
            }

        except FileNotFoundError:
            return {"success": False, "msg": f"Invalid Directory: {alerts_dir}"}
        except PermissionError:
            return {"success": False, "msg": f"Access Denied to: {alerts_dir}"}
        except Exception as e:
            return {"success": False, "msg": f"An unexpected error occurred: {e}"}


AlertSystem = Alert(working_dir="synapsis_dev", university_name="IU")
format_print(AlertSystem.directory_setup(synapsis_dir="synapsis"))
format_print(AlertSystem.load_system_list(system_list_file="systemList.txt"))
format_print(AlertSystem.move_custom_alerts())
