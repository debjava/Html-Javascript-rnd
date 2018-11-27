package com.ddlab.rnd.tornado.action;

import java.io.File;
import java.util.Iterator;

import org.eclipse.core.resources.IFile;
import org.eclipse.core.resources.IFolder;
import org.eclipse.core.resources.IProject;
import org.eclipse.core.resources.IProjectDescription;
import org.eclipse.core.runtime.CoreException;
import org.eclipse.core.runtime.IAdaptable;
import org.eclipse.jface.action.IAction;
import org.eclipse.jface.dialogs.MessageDialog;
import org.eclipse.jface.viewers.ISelection;
import org.eclipse.jface.viewers.IStructuredSelection;
import org.eclipse.swt.widgets.Shell;
import org.eclipse.ui.IObjectActionDelegate;
import org.eclipse.ui.IWorkbenchPart;

public class ToggleNatureAction implements IObjectActionDelegate {

	private ISelection selection;
	
	private void executeCmd( String command , String folderPath )
	{
		try 
		{
			String[] ss = folderPath.split("/");
			String val = "";
			for( String s : ss )
			{
				val = val+s+File.separator;
			}
			System.out.println("val---->"+val);
			command = command+val;
			Process process = Runtime.getRuntime().exec(command);
			process.waitFor();
			process.destroy();
		}
		catch (Exception e) 
		{
			e.printStackTrace();
			MessageDialog.openError( new Shell(), "Error", "Unexpected Error.\nReport to debadatta.mishra@gmail.com");
		}
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see org.eclipse.ui.IActionDelegate#run(org.eclipse.jface.action.IAction)
	 */
	public void run(IAction action) 
	{
		if (selection instanceof IStructuredSelection) 
		{
			for (Iterator it = ((IStructuredSelection) selection).iterator(); it
					.hasNext();) 
			{
				Object element = it.next();
				IFile ifile = null;
				if(element instanceof IFile)
				{
					ifile = (IFile) element;
					String folderPath = ifile.getLocationURI().getPath();
					folderPath = folderPath.startsWith("/") ? folderPath.substring(folderPath.indexOf("/")+1,folderPath.length()) : folderPath ;
					System.out.println("Folder path :::"+folderPath);
					String command = "explorer.exe /select,";
					executeCmd(command, folderPath);
				}
				IFolder ifolder = null;
				if( element instanceof IFolder )
				{
					ifolder = (IFolder) element;
					String folderPath = ifolder.getLocationURI().getPath();
					folderPath = folderPath.startsWith("/") ? folderPath.substring(folderPath.indexOf("/")+1,folderPath.length()) : folderPath ;
					System.out.println("Folder path :::"+folderPath);
					String command = "explorer.exe /root,";
					executeCmd(command, folderPath);
				}
				IProject project = null;
				if (element instanceof IProject) 
				{
					project = (IProject) element;
					String folderPath = project.getLocationURI().getPath();
					folderPath = folderPath.startsWith("/") ? folderPath.substring(folderPath.indexOf("/")+1,folderPath.length()) : folderPath ;
					System.out.println("Folder path :::"+folderPath);
					String command = "explorer.exe /root,";
					executeCmd(command, folderPath);
				}
				else if (element instanceof IAdaptable) 
				{
					project = (IProject) ((IAdaptable) element)
							.getAdapter(IProject.class);
				}
				if (project != null) 
				{
					toggleNature(project);
				}
			}
		}
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see org.eclipse.ui.IActionDelegate#selectionChanged(org.eclipse.jface.action.IAction,
	 *      org.eclipse.jface.viewers.ISelection)
	 */
	public void selectionChanged(IAction action, ISelection selection) {
		this.selection = selection;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see org.eclipse.ui.IObjectActionDelegate#setActivePart(org.eclipse.jface.action.IAction,
	 *      org.eclipse.ui.IWorkbenchPart)
	 */
	public void setActivePart(IAction action, IWorkbenchPart targetPart) {
	}

	/**
	 * Toggles sample nature on a project
	 * 
	 * @param project
	 *            to have sample nature added or removed
	 */
	private void toggleNature(IProject project) {
		try {
			IProjectDescription description = project.getDescription();
			String[] natures = description.getNatureIds();

			for (int i = 0; i < natures.length; ++i) {
				if (FolderOpener.NATURE_ID.equals(natures[i])) {
					// Remove the nature
					String[] newNatures = new String[natures.length - 1];
					System.arraycopy(natures, 0, newNatures, 0, i);
					System.arraycopy(natures, i + 1, newNatures, i,
							natures.length - i - 1);
					description.setNatureIds(newNatures);
					project.setDescription(description, null);
					return;
				}
			}

			// Add the nature
			String[] newNatures = new String[natures.length + 1];
			System.arraycopy(natures, 0, newNatures, 0, natures.length);
			newNatures[natures.length] = FolderOpener.NATURE_ID;
			description.setNatureIds(newNatures);
			project.setDescription(description, null);
		} catch (CoreException e) {
		}
	}

}
