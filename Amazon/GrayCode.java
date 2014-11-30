public class GrayCode {
    public static int grayCode(byte term1, byte term2) {
        if (term1 == term2) {
            return 0;
        }
        byte checker = (byte) (term1 ^ term2);
        //byte result = (byte) (checker & (checker - (byte) 0x1));
        //return (result == (byte) 0x0) ? 1 : 0;
        return ((byte) (checker & (checker - (byte) 0x1)) == (byte) 0x0) ? 1 : 0;
    }
    public static void main(String[] args) {
        System.out.println(grayCode((byte) 3, (byte) 2));
    }
}
