from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

# you can also import SoftwareEngine, HardwareType, SoftwareType, Popularity from random_user_agent.params
# you can also set number of user agents required by providing `limit` as parameter
software_names = [SoftwareName.CHROMIUM.value,
                  SoftwareName.FIREFOX.value,
                  SoftwareName.CHROME.value,
                  SoftwareName.OPERA.value]

operating_systems = [OperatingSystem.CHROMEOS.value,
                     OperatingSystem.MACOS.value,
                     OperatingSystem.LINUX.value,
                     OperatingSystem.ANDROID.value]

user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=1000)


# Get list of user agents.
def GetAll():
    return user_agent_rotator.get_user_agents()


# Get Random User Agent String.
def GetRandom():
    return user_agent_rotator.get_random_user_agent()
