import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
public class Solution {
    public static void main(String args[]) throws Exception {
        List<Iterator<String>> lists = new Arrays<>();
        lists.add(Arrays.asList("a", "b", "c").iterator());
        lists.add(null);
        lists.add(Arrays.<String>asList().iterator());
        lists.add(Arrays.asList("d", "e").iterator());
        lists.add(Arrays.<String>asList().iterator());

        Iterator<Iterator<String>> iters = lists.iterator();
        Iterator<String> flattened = flatten(iters);
        while (flattened.hasNext()) {
            System.out.println(flatten.next());
        }
    }
    public static Iterator<String> flatten(Iterator<Iterator<String>> iterator) {
        return null;
    }
}
public static Iterator<String> flatten(final Iterator<Iterator<String>> iters) {
    return new Iterator<String>() {
        private Iterator<String> curIter = null;
        private String nextItem = advanceItem();
        private String advanceItem() {
            if (iters == null && curIter == null) throw new NullPointerException();
            while ((iters != null && iters.hasNext()) || (curIter != null && curIter.hasNext())) {
                if ((curIter == null || !curIter.hasNext())) {
                    if (iters != null && iters.hasNext()) {
                        curIter = iters.next();
                    }
                }
                if (curIter == null) {
                    continue;
                }
                while (curIter.hasNext()) {
                    String result = curIter.next();
                    if (result != null) {
                        return result;
                    }
                }
            }
            return null;
        }
        public boolean hasNext() {
            return nextItem != null;
        }
        public String next() {
            if (!hasNext()) {
                throw new NullPointerException();
            }
            String oldItem = nextItem;
            nextItem = advanceItem();
            return oldItem;
        }
        public void remove() {
            throw new UnsupportedOperationException();
        }
    }
}

private static Map<Integer, Integer> calculateDegreeCount(Node node) {
    Queue<Node> bfsQ = new LinkedList<Node>();
    HashSet<Node> visted = new HashSet<Node>();
    HashSet<Integer, Integer> res = new HashSet<Integer, Integer>();
    bfsQ.add(node);
    visted.add(node);
    while(!bfsQ.isEmpty()) {
        Node temp = bfsQ.remove();
        int count = 0;
        for (Node neighbor : temp.neighbors) {
            count += 1;
            if (visted.contains(neighbor)) {
                visted.add(neighbor);
                bfsQ.add(neighbor)
            }
        }
        if (res.containsKey(count)) {
            int prevCount = res.get(count);
            res.put(count, prevCount + 1);
        } else {
            res(count, 1)
        }
    }
    return res;
}
