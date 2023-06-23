#/bin/bash
# Creacted by W2k8

# Set errorcode on error
# if checks fails, throw an error
let exit_code=2

for image in $(sudo docker ps -q)
do
  image_state=$(sudo docker inspect $image | jq .[0].State.Status | cut -c2- | rev | cut -c2- | rev)
  image_name=$(sudo docker inspect $image | jq .[0].Config.Image)
  echo "$image_name is $image_state"
  if [ "$image_state" = "runnning" ]
    then exit_code=0
  fi
  if [ $image_state != "runnning" ]
    then running_docker=="Error"
  fi
done
if [ $running_docker = "Error" ]
  then exit_code=2
fi

exit=$exitcode
