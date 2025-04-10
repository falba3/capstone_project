import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('UploadDonorData function triggered.')
    return func.HttpResponse("Hello from Azure Function!", status_code=200)
