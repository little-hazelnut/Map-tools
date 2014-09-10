/*	������Դ����·����ʶ������ʵ��
 * 	Դ�ļ����ƣ�PointToMarsMarkMap.java
 *	Ҫ  �㣺
 *		���ݱ�׼���긡������������KML��ʽ�ļ�,���ɻ�������·��,��google earth�򿪴�KML��
 *		���ɵ������ļ�ΪMars����
 *		�������PointToMarsMarkKML.java
 */
 
import java.io.File;
import java.awt.Desktop;
import java.io.IOException;

public class PointToMarsMarkMap{

	private String src = "";
	private String dest = "";
	private File KMLfile = null;
	
	PointToMarsMarkMap(String src,String dest){
		this.src = src;
		this.dest = dest;
	}
	
	public void loadKML(){
		Desktop desktop = Desktop.getDesktop();
		try{
			desktop.open(KMLfile);
		}catch(IOException e){
			e.printStackTrace();
		}
	}
	
	public void creatKML(){
		PointToMarsMarkKML ptmmk = new PointToMarsMarkKML(src,dest);
		KMLfile = ptmmk.creatKML();
	}
	
	public static void main(String[] args){
		String srcFile = "carID2622206.txt";
		String destFile = "carID2622206_mars.kml";
		PointToMarsMarkMap ptmmm = new PointToMarsMarkMap(srcFile,destFile);
		ptmmm.creatKML();
		ptmmm.loadKML();
	}
	
}