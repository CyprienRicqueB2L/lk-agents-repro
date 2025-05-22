echo "Warning: This will terminate all 'livekit' and 'python -m' processes."
read -p "Are you sure you want to proceed? (y/n): " confirm

if [ "$confirm" = "y" ]; then
    ps -ef | grep 'livekit' | grep -v grep | awk '{print $2}' | xargs -r kill -9
    ps -ef | grep 'python -m' | grep -v grep | awk '{print $2}' | xargs -r kill -9
else
    echo "Operation cancelled."
fi
