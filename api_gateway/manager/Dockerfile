FROM pantsel/konga:0.14.9

COPY certs/localhost.crt /certs/localhost.crt
COPY certs/localhost.key /certs/localhost.key

# https://github.com/pantsel/konga/blob/master/docs/SEED_DEFAULT_DATA.md
COPY manager/data/user.data /app/kongadata/uploads/user.data
COPY manager/data/node.data /app/kongadata/uploads/node.data

