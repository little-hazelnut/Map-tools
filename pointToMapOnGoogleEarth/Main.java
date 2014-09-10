public class Main{
	public static void main(String[] args){
		if(args.length != 2){
			System.out.println("Please input src");
			System.exit(-1);
		}
		String srcFile = args[0];
		String destFile = args[1];
		PointToMarkMap ptmm = new PointToMarkMap(srcFile,destFile);
		ptmm.creatKML();
		ptmm.loadKML();
	}
}