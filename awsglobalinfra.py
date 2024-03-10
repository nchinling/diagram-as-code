from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB

cluster_attr = {
    "fontsize": "15",
    "bgcolor": "transparent",
}

block_attr = {
    "fontsize": "15",
    "bgcolor": "lightgreen",

}

with Diagram("AWS Global Infrastructure"):
    with Cluster("AWS Cloud", graph_attr=cluster_attr):

        with Cluster("Region", graph_attr=cluster_attr):
            lb = ELB("lb")
            with Cluster("Availability Zone 1", graph_attr=block_attr) as az_1:
                az1_resource = EC2("AWS Resources")

            with Cluster("Availability Zone 2", graph_attr=block_attr) as az_2:
                az2_resource = EC2("AWS Resources")
            lb >> [az1_resource, az2_resource]
