/*	������Դ����·����ʶ������ʵ��
 * 	Դ�ļ����ƣ�PointToMarkMap.java
 *	Ҫ  �㣺
 *		���ݱ�׼���긡������������KML��ʽ�ļ�,���ɱ�׼����㣬��google earth�򿪴�KML��
 *		�������PointToMarkKML.java
 */
 
import java.io.File;
import java.awt.Desktop;
import java.io.IOException;

public class PointToMarkMap{

	private String src = "";
	private String dest = "";
	private File KMLfile = null;
	
	PointToMarkMap(String src,String dest){
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
		PointToMarkKML ptmk = new PointToMarkKML(src,dest);
		KMLfile = ptmk.creatKML();
	}
	
	/*
	public static void main(String[] args){
		String srcFile = "20131201JinAnSouthRoad.txt";
		String destFile = "20131201JinAnSouthRoad.kml";
		PointToMarkMap ptmm = new PointToMarkMap(srcFile,destFile);
		ptmm.creatKML();
		ptmm.loadKML();
	}
	*/
}