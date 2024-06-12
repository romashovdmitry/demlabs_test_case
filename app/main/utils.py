""" small helper-functions that could be used in several or all apps """
# Python imports
import logging


logger = logging.getLogger(__name__)


def define_image_file_path(
        filename: str,
        directory: str,
        object_type: str,
        instance_indicator: str
):
    """
    Define path for uploaded to API image.

    Parameters:
        filename: string with name of file
        directory: path where photoes are saved
            inside media directory
        instance: object of model Player, Club
            or another
    Returns:
        str: filename that would be used for
            saving file in project
            
    """
    try:
        return directory + instance_indicator + object_type + filename.split(".")[-1]

    except Exception as ex:
        logger.error(
            f'main.utils.define_image_file_path: {ex}'
        )

        return filename

