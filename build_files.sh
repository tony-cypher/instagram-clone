# install python in the vercel environment
apt-get update && apt-get install -y python3 python3-pip

# install required packages
pip3 install -r requirements.txt

# Run Django collectstatic
python3.9 manage.py collectstatic --noinput