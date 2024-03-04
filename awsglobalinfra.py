from diagrams import Diagram, Cluster
from diagrams.aws.iot import IotAnalyticsDataStore

with Diagram("AWS Global Infrastructure", show=True):
    with Cluster("AWS Cloud"):

        with Cluster("Regions"):
            with Cluster("Availability Zone 2") as az_2:
                az1_resource = IotAnalyticsDataStore("AWS Resources")

            with Cluster("Availability Zone 1") as az_1:
                az2_resource = IotAnalyticsDataStore("AWS Resources")
