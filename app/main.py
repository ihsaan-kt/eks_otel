import time
import random
import logging

from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk._logs import LoggingHandler, LoggerProvider
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metrics_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter

# Set up OpenTelemetry Resource
resource = Resource(attributes={
    "service.name": "python-observability-app",
    "host.name": "localhost",
})

# -------- Tracing --------
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)
span_processor = BatchSpanProcessor(OTLPSpanExporter(endpoint="http://aws-otel-collector:4317", insecure=True))
trace.get_tracer_provider().add_span_processor(span_processor)

# -------- Metrics --------
metrics.set_meter_provider(MeterProvider(resource=resource))
meter = metrics.get_meter(__name__)
counter = meter.create_counter("demo_counter")

metric_exporter = OTLPMetricExporter(endpoint="http://aws-otel-collector:4317", insecure=True)
metrics.get_meter_provider().start_pipeline(meter, metric_exporter, 5)

# -------- Logging --------
logger_provider = LoggerProvider(resource=resource)
log_exporter = OTLPLogExporter(endpoint="http://aws-otel-collector:4317", insecure=True)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))
handler = LoggingHandler(level=logging.INFO, logger_provider=logger_provider)
logging.basicConfig(level=logging.INFO, handlers=[handler])

logger = logging.getLogger(__name__)

# -------- App Logic --------
if __name__ == "__main__":
    while True:
        with tracer.start_as_current_span("process_task") as span:
            logger.info("collecting logs...")
            logger.info("collecting metrics...")
            logger.info("collecting traces...")
            counter.add(1)
            time.sleep(random.uniform(0.3, 1.2))
