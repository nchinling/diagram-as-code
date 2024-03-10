from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.onprem.database import MySQL
from diagrams.onprem.database import MongoDB
from diagrams.onprem.inmemory import Redis
from diagrams.aws.general import InternetGateway

with Diagram("Trading system"):
    # ELB("lb") >> EC2("web") >> RDS("userdb")
    with Cluster("DB") as db:
        sql = MySQL("MySQL")
        mongo = MongoDB("MongoDB")
        redis = Redis("Redis cache")
    with Cluster("VPC") as vpc:
        ig = InternetGateway("Internet gateway")
        lb = ELB("lb")
        backend = EC2("backend")
        backend2 = EC2("backend 2")
    client = EC2("client")
    lb >> [backend, backend2]
    redis >> [backend, backend2]
    sql >> [backend, backend2]
    mongo >> [backend, backend2]
    client >> ig
    ig >> lb
    lb >> ig
    ig >> client
