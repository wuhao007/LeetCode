public class RightRotation {
    public static int rightRotation(String word1, String word2) {
        if (word1 == null || word2 == null) {
            return -1;
        } else if (word1.length() != word2.length() || word1.length() == 0) {
            return -1;
        } else {
            if ((word1 + word1).contains(word2)) {
                return 1;
            } else {
                return -1;
            }
        }
    }
    public static void main(String[] args) {
        System.out.println(rightRotation("helloworld", "worldhello"));
    }
}
