import argparse
import googleapiclient.discovery

# [START list_instances]
def list_instances(compute, project):
    result = compute.instances().list(project=project,zone='asia-southeast1-b').execute()
    return result['items'] if 'items' in result else None
# [END list_instances]


def main(project):
    compute = googleapiclient.discovery.build('compute', 'v1')

    instances = list_instances(compute, project)

    print('Instances in project %s ' % (project))
    for instance in instances:
        print(' - ' + instance['name'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Your Google Cloud project ID.')
   
    args = parser.parse_args()

    main(args.project_id)
