public class DeleteVowels {
    public static String deleteVowels(String s) {
        if (s == null) {
            return null;
        }
        //StringBuilder result = new StringBuilder();
        StringBuffer result = new StringBuffer();
        String v = "aeiouAEIOU";
        for (int i = 0; i < s.length(); i++) {
            char currChar = s.charAt(i);
            /*
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
            */
            if (v.indexOf(currChar) == -1) {
                result.append(currChar);
            }
        }
        return result.toString();
    }
    public static void main(String[] args) {
        String s = "oqueorcmv,meprjotqwrnnkahdfi";
        System.out.println(deleteVowels(s));
    }
}
