import os
import imghdr

def PictureNameFormater(Path,Filer='/',Jpeg='jpg'):
	SourcePath=Path
	if os.path.isfile(Path):
		Type=imghdr.what(Path)
		if Type==None:
			print 'Not a picture file.'
		else:
			if Type=='jpeg':
				Type=Jpeg
			PathList=Path.split(Filer)
			FileName=PathList[-1]
			FileNameList=FileName.split('.')
			if len(FileNameList)!=1:
				FileNameList[-1]=Type
			else:
				FileNameList.append(Type)
			FileName='.'.join(FileNameList)
			PathList[-1]=FileName
			Path=Filer.join(PathList)
			try:
				os.renames(SourcePath,Path)
			except WindowsError:
				PathList=Path.split('.')
				PathList[-2]=PathList[-2]+'_0'
				Path='.'.join(PathList)
				os.renames(SourcePath,Path)

if __name__ =='__main__':	
	List=os.listdir('.')
	for File in List:
		PictureNameFormater(File)