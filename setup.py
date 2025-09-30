from setuptools import setup, find_packages

setup(
    name='ProjectRoadGuardian',
    version='1.0.0',
    author='Mayank Paul,
    description='An AI-powered system for automated pothole detection and reporting.',
    
    # This automatically finds all your Python code packages
    packages=find_packages(),
    
    # This is the list of libraries your project depends on
    install_requires=[
        'ultralytics',
        'opencv-python-headless',
        'streamlit',
        'pandas',
        'numpy'
    ],
    
    python_requires='>=3.9',
)
