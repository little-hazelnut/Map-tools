/*	������Դ����·����ʶ������ʵ��
 * 	Դ�ļ����ƣ�PointToMarsLineMap.java
 *	Ҫ  �㣺
 *		���ݱ�׼���긡������������KML��ʽ�ļ�,���ɻ�������·��,��google earth�򿪴�KML��
 *		���ɵ������ļ�ΪMars����
 *		�������PointToMarsLineKML.java
 */
 
import java.io.File;
import java.awt.Desktop;
import java.io.IOException;

public class PointToMarsLineMap{

	private String src = "";
	private String dest = "";
	private File KMLfile = null;
	
	PointToMarsLineMap(String src,String dest){
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
		PointToMarsKML ptmk = new PointToMarsKML(src,dest);
		KMLfile = ptmk.creatKML();
	}
	
	public static void main(String[] args){
		String srcFile = "carID2622206.txt";
		String destFile = "carID2622206_mars.kml";
		PointToMarsLineMap ptmlm = new PointToMarsLineMap(srcFile,destFile);
		ptmlm.creatKML();
		ptmlm.loadKML();
	}
	
}