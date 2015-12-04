.. code::

        $ curl https://dfw.servers.api.rackspacecloud.com/v2/$account/servers \
           -X POST \
           -H "X-Auth-Project-Id: $account" \
           -H "Content-Type: application/json" \
           -H "Accept: application/json" \
           -H "X-Auth-Token: $token" \
           -d '{"server": {"name": "my_server_with_network", "imageRef": "d42f821e-c2d1-4796-9f07-af5ed7912d0e", "flavorRef": "2", "max_count": 1, "min_count": 1, "networks": [{"uuid": "538a112a-34d1-47ff-bf1e-c40639e886e2"}, {"uuid": "00000000-0000-0000-0000-000000000000"}, {"uuid": "11111111-1111-1111-1111-111111111111"}]}}' \
          | python -m json.tool