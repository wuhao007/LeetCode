public class Memcache {

    private Map<Integer, int[]> map;
    public Memcache() {
        // Initialize your data structure here.
        map = new HashMap<Integer, int[]>();
    }

    public int get(int curtTime, int key) {
        // Write your code here
        int[] temp;
        if (map.containsKey(key)) {
            temp = map.get(key);
        } else {
            return Integer.MAX_VALUE;
        }

        if (curtTime >= temp[1] && temp[1] != 0) {
            return Integer.MAX_VALUE;
        } else {
            return temp[0];
        }
    }

    public void set(int curtTime, int key, int value, int ttl) {
        // Write your code here
        int expire = curtTime + ttl;
        if (ttl == 0) {
            expire = 0;
        }
        int[] val = {value, expire};
        map.put(key, val);
    }

    public void delete(int curtTime, int key) {
        // Write your code here
        if (!map.containsKey(key)) {
            return;
        } else {
            map.remove(key);
        }
    }

    public int incr(int curtTime, int key, int delta) {
        // Write your code here
        if (!map.containsKey(key)) {
            return Integer.MAX_VALUE;
        }
        if (curtTime >= map.get(key)[1] && map.get(key)[1] != 0) {
            return Integer.MAX_VALUE;
        } else {
            int temp = map.get(key)[0];
            temp += delta;
            int[] val = {temp, map.get(key)[1]};
            map.put(key, val);
            return temp;
        }
    }

    public int decr(int curtTime, int key, int delta) {
        // Write your code here
        if (!map.containsKey(key)) {
            return Integer.MAX_VALUE;
        }
        if (curtTime >= map.get(key)[1] && map.get(key)[1] != 0) {
            return Integer.MAX_VALUE;
        } else {
            int temp = map.get(key)[0];
            temp -= delta;
            int[] val = {temp, map.get(key)[1]};
            map.put(key, val);
            return temp;
        }
    }
}
