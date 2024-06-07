import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
public class RijndaelEncryption {
 private static final String ALGORITHM = "AES";
 public static byte[] encrypt(byte[] key, byte[] data) throws Exception {
 SecretKeySpec secretKey = new SecretKeySpec(key, ALGORITHM);
 Cipher cipher = Cipher.getInstance(ALGORITHM);
 cipher.init(Cipher.ENCRYPT_MODE, secretKey);
 return cipher.doFinal(data);
 }
 public static byte[] decrypt(byte[] key, byte[] encryptedData) throws Exception {
 SecretKeySpec secretKey = new SecretKeySpec(key, ALGORITHM);
 Cipher cipher = Cipher.getInstance(ALGORITHM);
 cipher.init(Cipher.DECRYPT_MODE, secretKey);
 return cipher.doFinal(encryptedData);
 }
 public static void main(String[] args) throws Exception {
 String data = "Hello, csbs!";
 String key = "SecretKey1234567";
 byte[] encryptedData = encrypt(key.getBytes(), data.getBytes());
 System.out.println("Encrypted data: " + new String(encryptedData));
byte[] decryptedData = decrypt(key.getBytes(), encryptedData);
 System.out.println("Decrypted data: " + new String(decryptedData));
 }
}
