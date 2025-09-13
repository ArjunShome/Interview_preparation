import argparse
from log import logger
from Process.processor import Processor
from fastapi import FastAPI, Request, status
from fastapi.exceptions import ResponseValidationError, RequestValidationError
from fastapi.responses import JSONResponse
import logging
import uvicorn


# import API routers
from api.routes.patient_registration_routes import router as patient_registration_router

# Define API Application
hospitalManagementSystem = FastAPI(
            title="Hospital Management System",
            description="APIs for Hospital Management Syste m",
            version="1.0.0"
        )

# Routers mount
hospitalManagementSystem.include_router(patient_registration_router)

# Response Validation Error handling
@hospitalManagementSystem.exception_handler(ResponseValidationError)
async def response_validation_exception_handler(request: Request, exc: ResponseValidationError):
    logging.exception(f"Response validation Failed for : {request.method}, {request.url.path} : {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": {
                "type": "ResponseValidationError",
                "message": "Response did not match the documented schema.",
                "details": exc.errors()
            }
        },
    )

def get_parser():
    parser = argparse.ArgumentParser(description="Argument PArser for Hospital Management System")
    # Todo: Add Arguments for the process
    parser.add_argument("-kp", "--kafka_producer", help="Trigger Kafka Producer Run", action="store_true")
    parser.add_argument("-kc", "--kafka_consumer", help="Trigger Kafka Consumer Run", action="store_true")
    parser.add_argument("-p", "--process_data", help="Trigger Spark Processing data flow", action="store_true")
    parser.add_argument("-s", "--start_api_server", help="Start FastAPI Server", action="store_true")
    parser.add_argument("-ui", "--start_starlette_ui", help="Start Starlette UI Server", action="store_true")

    return parser

def main():
    args = get_parser().parse_args()
    if args.kafka_producer:
        from kafka.kafka import KafkaProducer
        producer = KafkaProducer()
        producer.run()
    if args.kafka_consumer:
        from kafka.kafka import KafkaConsumer
        consumer = KafkaConsumer()
        consumer.run()
    if args.process_data:
        processor = Processor()
        processor.read_stream()
    if args.start_api_server:
        uvicorn.run("main:hospitalManagementSystem", host="127.0.0.1", port=8000, reload=True)
    if args.start_starlette_ui:
        from UI.starlett_frontend import starlette_app
        uvicorn.run(starlette_app, host="127.0.0.1", port=8050)

    # Todo: Add Exception handling in Application level


if __name__ == "__main__":
    logger.info("Starting Application")
    main()
