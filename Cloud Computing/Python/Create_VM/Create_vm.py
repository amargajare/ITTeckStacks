from google.cloud import compute_v1
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

INSTANCE_NAME = 'myfirst-instance-gajare1'
MACHINE_TYPE = 'zones/us-central1-a/machineTypes/n1-standard-1'
SUBNETWORK = 'regions/us-central1/subnetwork/default'
SOURCE_IMAGE = 'projects/debian-cloud/global/images/family/debian-10'
NETWORK_INTERFACE = {
      'subnetwork': SUBNETWORK,
      'access_config': [ {'name': 'External NAT'} ]
}

compute_client = compute_v1.InstancesClient()

config = {

        'name': INSTANCE_NAME,
        'machine_type': MACHINE_TYPE,
       'disks': [{
                'boot': True,
                'autoDelete': True,
                'initializeParams': { 'source_image': SOURCE_IMAGE}
                    }
                 ],
        'network_interfaces': [NETWORK_INTERFACE]
        }

operation = compute_client.insert(
                project='tt-dev-001',
                zone='us-central-a',
                instance_resource=config
            )

operation.result()
print(f'Created VM instances:{INSTANCE_NAME}')
