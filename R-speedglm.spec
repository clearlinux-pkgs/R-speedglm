#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-speedglm
Version  : 0.3.2
Release  : 10
URL      : https://cran.r-project.org/src/contrib/speedglm_0.3-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/speedglm_0.3-2.tar.gz
Summary  : Fitting Linear and Generalized Linear Models to Large Data Sets
Group    : Development/Tools
License  : GPL-2.0
Requires: R-biglm
BuildRequires : R-biglm
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n speedglm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523743458

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523743458
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library speedglm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library speedglm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library speedglm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library speedglm|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/speedglm/DESCRIPTION
/usr/lib64/R/library/speedglm/INDEX
/usr/lib64/R/library/speedglm/Meta/Rd.rds
/usr/lib64/R/library/speedglm/Meta/data.rds
/usr/lib64/R/library/speedglm/Meta/features.rds
/usr/lib64/R/library/speedglm/Meta/hsearch.rds
/usr/lib64/R/library/speedglm/Meta/links.rds
/usr/lib64/R/library/speedglm/Meta/nsInfo.rds
/usr/lib64/R/library/speedglm/Meta/package.rds
/usr/lib64/R/library/speedglm/NAMESPACE
/usr/lib64/R/library/speedglm/NEWS
/usr/lib64/R/library/speedglm/R/speedglm
/usr/lib64/R/library/speedglm/R/speedglm.rdb
/usr/lib64/R/library/speedglm/R/speedglm.rdx
/usr/lib64/R/library/speedglm/data/data1.RData
/usr/lib64/R/library/speedglm/help/AnIndex
/usr/lib64/R/library/speedglm/help/aliases.rds
/usr/lib64/R/library/speedglm/help/paths.rds
/usr/lib64/R/library/speedglm/help/speedglm.rdb
/usr/lib64/R/library/speedglm/help/speedglm.rdx
/usr/lib64/R/library/speedglm/html/00Index.html
/usr/lib64/R/library/speedglm/html/R.css
