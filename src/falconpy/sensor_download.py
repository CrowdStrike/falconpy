from ._util import service_request, generate_error_result
from ._service_class import ServiceClass

class Sensor_Download(ServiceClass):

    def GetCombinedSensorInstallersByQuery():
        pass

    def DownloadSensorInstallerById(_id: str):
        # _id is the sha256 of the sensor
        pass

    def GetSensorInstallersEntities():
        pass

    def GetSensorInstallersCCIDByQuery():
        pass

    def GetSensorInstallersByQuery():
        pass