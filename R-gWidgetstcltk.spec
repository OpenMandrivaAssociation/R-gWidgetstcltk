%global packname  gWidgetstcltk
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.0_48
Release:          1
Summary:          Toolkit implementation of gWidgets for tcltk package
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-48.tar.gz
Requires:         R-methods R-gWidgets R-tcltk R-tcltk2 R-digest 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-gWidgets R-tcltk R-tcltk2 R-digest
BuildRequires:    x11-server-xvfb

%description
Port of the gWidgets API to the tcltk package. Requires TK 8.5 or greater
for the tile (ttk)widgets http://www.tcl.tk/software/tcltk/8.5.tml. This
is the default on Windows. Under linux, Tk must be installed. Under Mac OS
X (10.5) there are two options: native Tk or X11. For the native one, Tk
must be upgraded. See www.tcl.tk to download source. Under the Mac it
compiles and installs cleanly. For X11, tcltk libraries can be downloaded
to augment the R binary package. See
http://cran.r-project.org/bin/macosx/tools/. The gdf function requires the
add on Tk package TkTable (http://tktable.sourceforge.net/).

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
xvfb-run %{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/images
%{rlibdir}/%{packname}/tcl
