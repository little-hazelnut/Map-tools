/*	程序来源：道路限速识别论文实验
 * 	源文件名称：PointToMarkMap.java
 *	要  点：
 *		根据标准坐标浮动车数据生成KML格式文件,生成标准坐标点，用google earth打开此KML。
 *		必须调用PointToMarkKML.java
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