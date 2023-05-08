%define debug_package %{nil}

%global gh_user rs

Name:           curlie
Version:        1.7.1
Release:        1
Summary:        The power of curl, the ease of use of httpie.
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
If you like the interface of HTTPie but miss the features of curl, curlie
is what you are searching for. Curlie is a frontend to curl that adds the
ease of use of httpie, without compromising on features and performance.
All curl options are exposed with syntax sugar and output formatting
inspired from httpie.

%prep
%setup -q -n %{name}-%{version}

%build
go build -o %{_builddir}/bin/%{name}

%install
install -Dm0755 %{_builddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue May 9 2023 Jamie Curnow <jc@jc21.com> 1.7.1-1
- https://github.com/rs/curlie/releases/tag/v1.7.1

* Mon Jun 21 2021 Jamie Curnow <jc@jc21.com> 1.6.0-1
- https://github.com/rs/curlie/releases/tag/v1.6.0


