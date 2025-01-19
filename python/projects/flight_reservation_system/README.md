# MEMO

### 初期設定

mysql connect

```
mysql -u educative -psecret flight
```

```
python3 /usercode/flight_reservation/repositories/tables.py
```

```
python3 /usercode/flight_reservation/repositories/seed.py
```

### 実装メモ

the breadth-first search (BFS) technique とは？？

This function will take date, departure_airport, destination_airport, and max_stops as parameters.

Initialize the following variables:

Create an empty list itinerary_list to store possible itineraries.

Use a deque (double-ended queue) for the BFS algorithm, initialized with a tuple containing departure_airport, an empty list for flights taken, None for the last arrival time, and a stop count of 0.

Create a set visited to keep track of airports already processed.

Now implement the BFS algorithm:

Create a while loop that continues as long as items are in the queue.

Pop from the queue to get the current airport, list of flights taken, the last flight’s arrival time, and the number of stops.

Skip the current branch if the airport is already visited or the number of stops exceeds max_stops.

Execute a database query to find all connecting flights departing from the current airport on the given date.

Loop through the fetched flights, and for each flight:

Ensure it’s not a direct flight by checking if the arrival port doesn’t match the destination.

Check if the current flight’s departure time is valid/feasible, i.e., it departs at least one hour after the last flight’s arrival time.

If the current flight reaches the destination, add it to itinerary_list.

If not, append it to the queue and continue BFS from the new airport.

After completing the BFS, return the itinerary_list containing all valid itineraries.

### Implement Dijkstra's algorithm
