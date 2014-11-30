public class DeleteVowels {
    public static String deleteVowels(String s) {
        if (s == null) {
            return null;
        }
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char currChar = s.charAt(i);
            switch (currChar) {
                case 'a':
                case 'A':
                case 'e':
                case 'E':
                case 'i':
                case 'I':
                case 'o':
                case 'O':
                case 'u':
                case 'U':
                    break;
                default:
                    result.append(currChar);
                    break;
            }
        }
        return result.toString();
    }
    public static void main(String[] args) {
        String s = "oqueorcmv,meprjotqwrnnkahdfi";
        System.out.println(deleteVowels(s));
    }
}
