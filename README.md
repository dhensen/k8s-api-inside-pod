# Job Scheduling from within a pod on Kubernetes

```
minikube start
eval $(minikube docker-env)
docker build -t k8s-app:v<version_number> .
vim k8s-app.yaml # edit version_number accordingly
kubectl apply -f k8s-app.yaml
kubectl expose deployment/k8s-app --type=LoadBalancer
```

# Sources
- https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/#accessing-the-api-from-a-pod
- https://github.com/lachie83/k8s-kubectl
- https://github.com/kubernetes/kubernetes/blob/master/examples/kubectl-container/pod.json

# Todo
1. Actually schedule a job
2. Make some ip's and ports configurable via env vars.
3. Look into letting minikube pull from a registry deployed inside the cluster:
   - https://github.com/kubernetes/minikube/blob/master/docs/insecure_registry.md
   - https://kubernetes.io/docs/getting-started-guides/minikube/#private-container-registries