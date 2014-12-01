public class RightRotation {
    public static int rightRotation(String word1, String word2) {
        if (word1 == null || word2 == null || word1.length() != word2.length() || word1.length() == 0) {
            return -1;
        } else {
            //return (word1 + word1).contains(word2)? 1 : -1; 
            return (word1 + word1).indexOf(word2) != -1 ? 1 : -1; 
        }
    }
    public static void main(String[] args) {
        System.out.println(rightRotation("helloworld", "worldhello"));
    }
}
