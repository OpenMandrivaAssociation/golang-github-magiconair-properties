# http://github.com/magiconair/properties
%global goipath         github.com/magiconair/properties
%global commit          0723e352fa358f9322c938cc2dadda874e9151a9

%gometa -i

Name:           %{goname}
Version:        1.7.0
Release:        10%{?dist}
Summary:        Java properties scanner for Go
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml
Patch0:         change-import-paths.patch

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(gopkg.in/check.v1)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
%patch0 -p1

%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 17 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-9.git0723e35
- Upload glide files

* Wed Mar 07 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-8.git0723e35
- Update to spec 3.0

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-7
- Switch to __go_ignore macro

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-6
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.7.0-1
- Bump to upstream 0723e352fa358f9322c938cc2dadda874e9151a9
  related: #1413067

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 1.5.3-5
- Polish the spec file
  resolves: #1413067

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-4
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.3-3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git6240095
- First package for Fedora
  resolves: #1270054
