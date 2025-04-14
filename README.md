[![Static Badge](https://img.shields.io/badge/Open_In-AI_Workbench-76B900)](https://build.nvidia.com/open-ai-workbench/aHR0cHM6Ly9naXRodWIuY29tL3JvbmFrYmFua2EvZ2V0dGluZy1zdGFydGVkLW5pbS13b3JrYmVuY2g=)

# Getting Started with NVIDIA NIM and Workbench
This is an [NVIDIA AI Workbench](https://www.nvidia.com/en-us/deep-learning-ai/solutions/data-science/workbench/) project to try out the observability capabilities of NVIDIA NIMs. It lets you:
* Run inference **locally** using Llama 3.2 3B Instruct **microservices** via [NVIDIA Inference Microservices (NIMs)](https://www.nvidia.com/en-us/ai/) on Docker
* Use the Gradio UI Chat application to interact with the hosted NIM
* Use Jupyter notebook to interact with the model using langchain
* Visualize the performance metrics and traces using Prometheus, Jaeger, and Grafana.

## Description
This Project has two main capabilities: 
1. **Docker compose** with the following:

   - NVIDIA llama 3.2 3B Instruct NIM
   - Opentelemetry collector
   - Prometheus
   - Grafana for visualization
   - Zipkin for Distributed Tracing Visualization
3. **Juptyerlab notebook** to interact with the deployed NVIDIA llama 3.2 3b NIM

## Get Started

1. Before Getting Started, create your NGC API key and add it to the environment variable under Environment -> Project Container -> variables.

2. The Next Step is to deploy our llama NIM and the rest of the stack using Docker Compose. Go to Environment -> Project Container -> Compose.
   Select `all` from the profiles to deploy the entire stack. You can also choose just the `nim` profile to deploy the Llama 3B model Inference Microservice.
   Click on the `Start` button to deploy the stack.

3. Wait for the containers to be up and running; this might take a while if you deploy it for the first time, as the llama model will take some time to start. Once all the containers are up and running, you will be able to access the following components using localhost.

    ### Accessing Grafana
    
    Grafana can be accessed locally by navigating to the following URL in your web browser:
    
    [http://localhost:3000](http://localhost:3000)
    
    For first-time login, default credentials (`admin/admin`) are included.

   ### Accessing Zipkin
    
    Zipkin can be accessed locally by navigating to the following URL in your web browser:
    
    [http://localhost:9411](http://localhost:9411)
    

