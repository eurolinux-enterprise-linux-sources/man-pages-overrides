%global debug_package   %{nil}

Summary: Complementary and updated manual pages
Name: man-pages-overrides
Version: 7.4.3
Release: 1%{?dist}
# license is the same as for the man-pages package
License: GPL+ and GPLv2+ and BSD and MIT and Copyright only and IEEE
Group: Documentation
# there is no public download location for this package
Source: man-pages-overrides-%{version}.tar.xz

Patch0: 1073718-mpo-7.1.0-open.2.patch
Patch1: 1086994-mpo-7.1.0-proc.5.patch
Patch2: 1112307-mpo-7.3.0-cciss.4.patch
Patch3: 1021967-mpo-7.1.0-socat.1.patch
Patch4: 1131853-mpo-7.1.0-proc.5-proc-fs-not-empty.patch
Patch5: 1085531-mpo-7.4.0-ipvsadm.8.patch
Patch6: 1255283-mpo-7.3.0-captest.8.patch
Patch7: 1129235-mpo-7.1.0-flock.2.patch
# aarch64 specific patch
Patch8: 1361588-recv-for-aarch64.patch
Patch9: 1263575-mpo-7.3.1-libpng.3-png.5.patch
Patch10: 1263636-mpo-7.4.0-cp.1-install.1-mkdir.1-mkfifo.1-mknod.1.patch
Patch11: 1316009-mpo-7.4.0-mcstransd.8.patch
Patch12: 1131939-mpo-7.1.0-charsets.7-nl_langinfo.3.patch
Patch13: 1131859-mpo-7.1.0-host.conf.5.patch
Patch14: 1269549-mpo-7.3.0-socket.7.patch
Patch15: 1274949-mpo-7.3.0-userhelper.8.patch
Patch16: 1278492-mpo-7.3.1-recv.2.patch
# aarch64 specific patch
Patch17: 1095371-clone-and-open-for-aarch64.patch
Patch18: 1197850-mpo-7.2.0-backport-thread-safety-information.patch
Patch19: 1120294-madvise.2-MADV_REMOVE-supports-more-filesystems.patch
Patch20: 1147718-resolv.conf.5-add-missing-no-tld-query.patch
Patch21: 1289915-mpo-7.3.0-nsswitch.conf.5.patch
Patch22: 1452424-mpo-7.4.2-stat.2.patch
Patch23: 1141874-mpo-7.2.0-mgetty-fix-typos-in-mgetty-s-man-pages.patch
Patch24: 1297898-mpo-7.3.0-prctl.2.patch
Patch25: 1222720-mpo-7.2.0-rtld-audit.7.patch
Patch26: 1312875-mpo-7.3.0-tcp.7.patch
Patch27: 1315605-mpo-7.3.1-recv.2-cmsg.3.patch
Patch28: 1330661-mpo-7.3.1-clone.2-fork.2.patch
Patch29: 1411979-mpo-7.4.0-memparse.1.patch
Patch30: 1337039-mpo-7.3.0-setfacl.1.patch
Patch31: 1263629-mpo-7.3.0-cp.1-install.1-mkdir.1-mkfifo.1-mknod.1.patch
Patch32: 1263632-mpo-7.3.0-cp.1-install.1-mkdir.1-mkfifo.1-mknod.1.patch
Patch33: 1263635-mpo-7.3.0-cp.1-install.1-mkdir.1-mkfifo.1-mknod.1.patch
Patch34: 1263637-mpo-7.3.0-cp.1-install.1-mkdir.1-mkfifo.1-mknod.1.patch
Patch35: 1360898-mpo-7.3.2-prctl.2-capabilities.7.patch
Patch36: 1390935-mpo-7.4.0-nsswitch.conf.5.patch
Patch37: 1404478-mpo-7.4.0-packet.7.patch
Patch38: 1452368-mpo-7.4.2-clone.2.patch

%description
A collection of manual ("man") pages to complement other packages or update
those contained therein. Always have the latest version of this package
installed.

%prep
%autosetup -p1

%build
%ifarch aarch64
    deprecated_pages="access alarm bdflush chmod chown creat dup2 epoll_create epoll_wait eventfd fork futimesat getdents getpgrp inotify_init lchown link mkdir mknod pause pipe poll readlink rename rmdir select send signalfd symlink sysctl time umount unlink uselib ustat utime utimes vfork wait4"
    cd man-pages/man2
    for page in $deprecated_pages; do
        cp deprecated.2 $page.2
    done
    mv ____clone.2 clone.2
    mv ____open.2 open.2
    mv ____recv.2 recv.2
%else
    rm man-pages/man2/deprecated.2
    rm man-pages/man2/____clone.2
    rm man-pages/man2/____open.2
    rm man-pages/man2/____recv.2
%endif


%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/overrides
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
for i in *; do
    if [[ -d "$i" ]]; then
        for j in $(ls "$i"); do
           if [[ -d "$i/$j" ]]; then
               mkdir -p "$RPM_BUILD_ROOT%{_mandir}/overrides/$j"
               for k in $(ls "$i/$j"); do
                   if [[ -d "$i/$j/$k" ]]; then
                       mkdir -p "$RPM_BUILD_ROOT%{_mandir}/overrides/$j/$k"
                       cp -f "$i/$j/$k"/* "$RPM_BUILD_ROOT%{_mandir}/overrides/$j/$k"
                   else
                       cp -f "$i/$j"/* "$RPM_BUILD_ROOT%{_mandir}/overrides/$j"
                   fi
               done
           else
              mkdir -p "$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$i"
              cp "$i/$j" "$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$i"
           fi
        done
    fi
done

%files
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/overrides/

%changelog
* Mon Jun 05 2017 Nikola Forró <nforro@redhat.com> - 7.4.3-1
- Upload new tarball
- copy_file_range.2: add new manpage
  resolves: #1458195

* Mon May 22 2017 Nikola Forró <nforro@redhat.com> - 7.4.2-1
- Upload new tarball
  related: #1435590
- stat.2: update to cover latest things used in RHEL7
  resolves: #1452424
- clone.2: document features related to namespaces
  resolves: #1452368

* Thu Apr 13 2017 Nikola Forró <nforro@redhat.com> - 7.4.1-1
- Upload new tarball
  related: #1435590
- remove bug fixed in original component: #1167833 (net-tools)

* Tue Mar 28 2017 Nikola Forró <nforro@redhat.com> - 7.4.0-1
- Upload new tarball
  resolves: #1435590
- remove bug fixed in original component: #1147568 (mailx)
- remove bug fixed in original component: #1147570 (mailx)
- remove bug fixed in original component: #1147565 (ecj)
- remove bug fixed in original component: #1349833 (paflib)
- ipvsadm.8: add missing option
  resolves: #1085531
- cp.1, install.1, mkdir.1, mkfifo.1, mknod.1: update security context options
  to reflect coreutils change
  resolves: #1263636
- mcstransd.8: fix typos
  resolves: #1316009
- memparse.1: remove incorrect description
  resolves: #1411979
- nsswitch.conf.5: add information about sss service
  resolves: #1390935
- packet.7: add missing socket options
  resolves: #1404478
- namespaces.7, pid_namespaces.7, user_namespaces.7: add new manpages
  resolves: #1377583

* Thu Sep 22 2016 Nikola Forró <nforro@redhat.com> - 7.3.2-2
- open.2: revert documenting O_TMPFILE option
  related: #1330740

* Wed Aug 03 2016 Nikola Forró <nforro@redhat.com> - 7.3.2-1
- Upload new tarball
  related: #1343004
- prctl.2, capabilities.7: document ambient capabilities
  resolves: #1360898

* Thu Jul 28 2016 Nikola Forró <nforro@redhat.com> - 7.3.1-1
- Upload new tarball
  related: #1343004
- remove bug fixed in original component: #1240948 (psacct)
- recv.2: add deprecation note about recv() syscall on aarch64
  resolves: #1361588
- libpng.3: fix invalid RFC URL
  related: #1263575
- recv.2: change description of flags argument also on aarch64
  related: #1278492
- localedef.1: add missing --old-style option
  related: #1301661
- recv.2: fix type of cmsg_len member of cmsghdr structure also on aarch64
  related: #1315605
- clone.2: document ERESTARTNOINTR error code also on aarch64
  related: #1330661
- open.2: document O_TMPFILE option also on aarch64
  related: #1330740

* Fri Jun 24 2016 Nikola Forró <nforro@redhat.com> - 7.3.0-1
- Upload new tarball
  resolves: #1343004
- remove bug fixed in original component: #1147538 (xinetd)
- remove bug fixed in original component: #1147550 (vsftpd)
- remove bug fixed in original component: #1147551 (vsftpd)
- remove bug fixed in original component: #1147552 (pam_krb5)
- remove bug fixed in original component: #1147572 (wget)
- remove bug fixed in original component: #1155006 (mc)
- remove bug fixed in original component: #1218284 (stunnel)
- remove bug fixed in original component: #1147564 (edac-utils)
- __fpurge.3: add missing man page
  resolves: #1267657
- cciss.4: replace man page content with notice about driver removal
  resolves: #1112307
- libpaf-dsc.3, libpaf-ebb.3: fix formatting and examples
  resolves: #1181670
- captest.8: describe --init-grp option
  resolves: #1255283
- png.5: fix invalid RFC URL
  resolves: #1263575
- socket.7: document SO_REUSEPORT option
  resolves: #1269549
- userhelper.8: fix up exit status description and consistency
  resolves: #1274949
- recv.2: change description of flags argument to apply also to recvfrom and recvmsg
  resolves: #1278492
- nsswitch.conf.5: add list of files being read when "files" service is used
  resolves: #1289915
- prctl.2: add description of Intel MPX calls
  resolves: #1297898
- iconv.1, locale.1, localedef.1, repertoiremap.5, iconvconfig.8: add new man pages
- charmap.5, locale.5, charsets.7, locale.7: sync with upstream
  resolves: #1301661
- tcp.7: document TCP_USER_TIMEOUT
  resolves: #1312875
- recv.2, cmsg.3: fix type of cmsg_len member of cmsghdr structure
  resolves: #1315605
- clone.2, fork.2: document ERESTARTNOINTR error code
  resolves: #1330661
- open.2: document O_TMPFILE option
  resolves: #1330740
- setfacl.1: document the meaning of '-' in perms
  resolves: #1337039
- cp.1, install.1, mkdir.1, mkfifo.1, mknod.1: update security context options
  to reflect coreutils change
  resolves: #1263629
- cp.1, install.1, mkdir.1, mkfifo.1, mknod.1: update security context options
  to reflect coreutils change
  resolves: #1263632
- cp.1, install.1, mkdir.1, mkfifo.1, mknod.1: update security context options
  to reflect coreutils change
  resolves: #1263635
- cp.1, install.1, mkdir.1, mkfifo.1, mknod.1: update security context options
  to reflect coreutils change
  resolves: #1263637

* Fri Sep 25 2015 jchaloup <jchaloup@redhat.com> - 7.2.4-1
- New patch for fpurge with MT introduced since the first evaluation
- Remove mkfifoat.3 man page
- Upload new tarball
  related: #1197850

* Tue Sep 22 2015 jchaloup <jchaloup@redhat.com> - 7.2.3-2
- Add missing man pages with symlink
- Upload new tarball
  related: #1197850

* Fri Sep 11 2015 jchaloup <jchaloup@redhat.com> - 7.2.2-1
- Add missing man pages to en/man3 directory
- Fix use of .SH ATTRIBUTE macro
  related: #1197850

* Wed Jul 08 2015 jchaloup <jchaloup@redhat.com> - 7.2.1-1
- Upload new tarball
  related: #1225032
- removed bug fixed in original component: #1147556 (mt-st)
- fix dump utmp name in dump-utmp.8
  resolves: #1164846

* Tue May 26 2015 jchaloup <jchaloup@redhat.com> - 7.2.0-1
- Upload new tarball
  resolves: #1225032
- removed bug fixed in original component: #1152066 (bind)
- removed bug fixed in original component: #1147545 (zsh)
- backport MT info from man-pages 3.81
  resolves: #1197850
- fix typoes in mgetty's man pages
  resolves: #1141874
- fix wrong usage of accept/connect options in stunnel.8
  resolves: #1155977
- autoconf: add missing config.guess.1 and config.sub.1 (no patch)
  resolves: #1162225
- rtld-audit.7 fix the correct format for cookies
  resolves: #1222720
- Don't generate debuginfo subpackage
  resolves: #1179262

* Tue Dec 16 2014 jchaloup <jchaloup@redhat.com> - 7.1.3-1
- resolver.5 is a redirection to resolv.conf
  upload the latest tarball
  related: #1147718
- procng-ng contains pl/pkill.1 man page which reffers non-existing one, removing the pl mutation
  related: #1150170

* Tue Nov 25 2014 jchaloup <jchaloup@redhat.com> - 7.1.2-1
- netstat.8 -S/--sctp options added
  resolves: #1064756
- latest tarball uploaded
- update ecj.1 man page to the latest upstream version
  related: #948442

* Thu Oct 16 2014 jchaloup <jchaloup@redhat.com> - 7.1.1-1
- deprecated syscalls for aarch64
  related: #1095371
- latest tarball uploaded
- delete system-config-bind text from named.8
  resolves: #1148758
- madvise.2 MADV_REMOVE supports more filesystems
  resolves: #1120294
- resolv.conf.5 add missing no-tld-query
  resolves: #1147718
- mc.1 fixing typos
  resolves: #948487
- missing fanotify manual pages added (in tarball)
  resolves: #1155260
- missing localized man-pages in procps-ng 3.3.10 added (in tarball)
  resolves: #1150170

* Mon Aug 11 2014 jchaloup <jchaloup@redhat.com> - 7.1.0-1
- resolves: #1095371
  deprecated syscalls for aarch64 (remove man page and its syscalls for non-aarch64 archs)
  latest tarball uploaded
- resolves: #1073718
  clarification of open.2 man page about aligned buffer size
- resolves: #1086994
  adding missing proc fields description
- resolves: #1040023
  ssl_request_cert formating typo in vsftpd.conf man page
- resolves: #1021967
  socat formating typo in man page
- resolves: #1131853
  proc/fs is not an empty directory
- resolves: #1146259
  information about xinitd reload
- resolves: #1104994
  missing isolate options in vsftpd.conf man page
- resolves: #1129235
  flock.2 more info about locks over NFS
- resolves: #948457
  mt.1 missing option section
- resolves: #948599
  edac-ctl.1 missing options
- resolves: #1109291
  mailx.1 additional information about FROM syntax
- resolves: #1109294
  mailx.1 additional information about environment variables
- resolves: #1131939
  charset.7, nl_langinfo.3 information about implicit codeset
- resolves: #1131859
  host.conf.5. multi on by default
- resolves: #1066917
  zsh.1, zshall.1 missing option for emulation
- resolves: #964302
  ignore_afs missing options in pam_krb5.8
- resolves: #1140589
  wget.1 duplicated options deleted
- resolves: #1069350
  wrong symlink in run-parts.4, cp crontabs.4 run-parts.4 (in tarball)
- resolves: #948442
  new man page for ecj.1 (in tarball)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 7.0.0-2
- Mass rebuild 2013-12-27

* Thu Oct 18 2012 Peter Schiffer <pschiffe@redhat.com> 7.0.0-1
- initial package for RHEL-7.0
