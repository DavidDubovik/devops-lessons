# Deployment Instructions

## Prerequisites
Ensure that you have access to a Kubernetes cluster and `kubectl` is configured properly.

## Deploying the DaemonSet
1. Apply the DaemonSet manifest:
   ```sh
   kubectl apply -f daemonset.yml
   ```
2. Verify that the DaemonSet is running on all nodes:
   ```sh
   kubectl get daemonset
   ```
3. Check the pods created by the DaemonSet:
   ```sh
   kubectl get pods -l app=<daemonset-label>
   ```

## Deploying the CronJob
1. Apply the CronJob manifest:
   ```sh
   kubectl apply -f cronjob.yml
   ```
2. Verify that the CronJob is created:
   ```sh
   kubectl get cronjob
   ```
3. Manually trigger a CronJob run (optional):
   ```sh
   kubectl create job --from=cronjob/<cronjob-name> <job-name>
   ```

## Validation
### DaemonSet Logs
Check logs from one of the DaemonSet pods:
```sh
kubectl logs -l app=<daemonset-label> --tail=50
```

### CronJob Logs
Check logs from a completed CronJob pod:
```sh
kubectl get pods --selector=job-name=<cronjob-name> --field-selector=status.phase=Succeeded
kubectl logs <cronjob-pod-name>
```

### Cleanup
To remove the resources:
```sh
kubectl delete -f daemonset.yml
kubectl delete -f cronjob.yml
```

