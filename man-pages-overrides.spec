Summary: Complementary and updated manual pages
Name: man-pages-overrides
Version: 6.6.3
Release: 2%{?dist}
# man - GPLv2
License: GPLv2
Group: Documentation
# there is no public download location for this package
Source0: man-pages-overrides-%{version}.tar.gz
Patch4: 657563-mpo-2.0-findutils.patch
Patch8: 619779-mpo-2.0-lftp.patch
Patch11: 615873-mpo-2.1-w3m.patch
Patch12: 675213-mpo-2.1-usermode.patch
Patch21: 712256-mpo-6.2.0-volume_key.patch
Patch28: 730042-mpo-6.2.2-cpufrequtils.patch
Patch30: 731690-mpo-6.2.2-ecryptfs-utils.patch
Patch37: 801742-mpo-6.3.2-keyutils.patch
Patch43: 801783-mpo-6.3.2-ebtables.patch
Patch45: 653908-mpo-6.3.2-setools.patch
Patch46: 872526-mpo-6.4.1-dump.patch
Patch47: 853959-mpo-6.4.1-rng-tools.patch
Patch48: 867332-mpo-6.4.1-shadow-utils.patch
Patch49: 806845-mpo-6.4.1-dmidecode.patch
Patch52: 846591-mpo-6.4.1-ipmitool.patch
Patch55: 807323-mpo-6.5.1-byzanz-record.patch
Patch57: 905066-mpo-6.5.1-curl-ca.patch
Patch58: 896544-mpo-6.5.1-curl-typos.patch
Patch62: 979460-mpo-6.5.1-mailx.patch
Patch63: 960281-mpo-6.5.1-man-pages-clock-getres.patch
Patch64: 974697-mpo-6.5.1-man-pages-ld-so.patch
Patch65: 953753-mpo-6.5.1-man-pages-proc-oom-adj.patch
Patch66: 953750-mpo-6.5.1-man-pages-proc-dmesg-restrict.patch
Patch67: 953539-mpo-6.5.1-man-pages-proc-kptr-restrict.patch
Patch68: 908295-mpo-6.5.1-man-pages-syslog.patch
Patch69: 974685-mpo-6.5.1-man-pages-sched_setaffinity-revert.patch
Patch70: 988125-mpo-6.5.1-man-pages-madvise.patch
Patch71: 903258-mpo-6.5.1-man-pages-fallocate.patch
Patch72: 957010-mpo-6.5.1-man-pages-strtoul.patch
Patch73: 928917-mpo-6.5.1-man-pages-open.patch
Patch74: 979318-mpo-6.5.1-net-tools.patch
Patch75: 951826-mpo-6.5.1-postfix.patch
Patch77: 983066-mpo-6.5.1-rhn-client-tools.patch
Patch80: 884699-mpo-6.5.1-usbutils.patch
Patch85: 1018622-mpo-6.5.2-arpwatch.patch
Patch86: 1039986-mpo-6.6.1-vsftpd.patch
Patch87: 1066537-mpo-6.6.1-zsh.patch
Patch88: 1058738-mpo-6.6.1-nscd.conf.patch
Patch89: 1058793-mpo-6.6.1-curl-wrong-nss-url.patch
Patch90: 735949-mpo-6.6.1-gimp-DESTDIR-removed.patch
Patch91: 988713-mpo-6.6.1-gzip-rsyncable-missing.patch
Patch92: 1058100-mpo-6.6.1-nscd.conf-default-settings.patch
Patch93: 1058349-mpo-6.6.1-getgrnam-buffer-size.patch
Patch94: 1075233-mpo-6.6.1-pcre.patch
Patch95: 1108028-mpo-6.6.2-openssl-ciphers.patch
Patch96: 1003511-mpo-6.6.2-nfs-utils-idmapd.patch
Patch97: 953741-mpo-6.6.2-man-pages-proc-proc-fs-not-empty-directory.patch
Patch98: 1114785-mpo-6.6.2-host.conf.patch
Patch99: 1099335-mpo-6.6.2-febootstrap-to-supermin.patch
# mail.1,nail.1,Mail.1 removed by patch. In new tar ball remove them and update this patch.
Patch100: 1099275-mpo-6.6.2-mailx.patch
# gtar.1 added by patch. In new tar ball add it and update this patch.
Patch101: 903666-mpo-6.6.2-tar.1.patch
Patch102: 1075152-mpo-6.6.2-xinted.patch
Patch103: 1017478-mpo-6.6.2-flock.patch
Patch104: 969502-mpo-6.6.2-rpm.patch
Patch105: 889049-mpo-6.6.2-vhostmd.patch
Patch106: 1087503-mpo-6.6.2-man-pages-codeset.patch
Patch107: 1112708-mpo-6.6.2-bash.patch
Patch108: 891928-mpo.6.6.2-man.patch
Patch109: 781499-mpo-6.6.2-makedeltarpm.patch

Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch
Requires: man >= 1.6f-24

%description
A collection of manual ("man") pages to complement other packages or update
those contained therein. Always have the latest version of this package
installed.

%prep
%setup -q -n %{name}-%{version}
%patch4 -p1
%patch8 -p1
%patch11 -p1
%patch12 -p1
%patch21 -p1
%patch28 -p1
%patch30 -p1
%patch37 -p1
%patch43 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch52 -p1
%patch55 -p1
%patch57 -p1
%patch58 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch77 -p1
%patch80 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
%patch93 -p1
%patch94 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%patch98 -p1
%patch99 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/overrides
mkdir -p $RPM_BUILD_ROOT%{_docdir}
for i in `ls`; do
    if [ -d $i ]
    then
        for j in `ls $i`; do
           if [ -d $i/$j ]
           then
               mkdir -p $RPM_BUILD_ROOT%{_mandir}/overrides/$j
               for k in `ls $i/$j`; do
                   if [ -d $i/$j/$k ]
                   then
                       mkdir -p $RPM_BUILD_ROOT%{_mandir}/overrides/$j/$k
                       cp -f $i/$j/$k/* $RPM_BUILD_ROOT%{_mandir}/overrides/$j/$k
                       gzip $RPM_BUILD_ROOT%{_mandir}/overrides/$j/$k/*
                   else
                       cp -f $i/$j/* $RPM_BUILD_ROOT%{_mandir}/overrides/$j
                   fi
               done
           else
              mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$i
              cp $i/$j $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/$i
           fi
        done
    fi
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}-%{version}
%{_mandir}/overrides

%changelog
* Mon Aug 04 2014 jchaloup <jchaloup@redhat.com> - 6.6.3-2
- related: #903666
  adding gtar.1 with link to tar.1
- related: #1099275
  removing mail.1, nail.1 and Mail.1

* Wed Jul 30 2014 jchaloup <jchaloup@redhat.com> - 6.6.3-1
- resolves: #1011892
  new man page for iconv.1
  patch 1003511-mpo-6.6.2-nfs-utils-rpc-idmapd.patch adding man page removed, man page in new tar
  patch 815680-mpo-6.6.2-lvm2-remove-man-pages.patch removing lmv2 man pages removed
  patch 964160-mpo-6.6.2-cracklib-cracklib-format.patch adding man page removed, man page in new tar
- related: #1058793
  url on a new line for both man pages
- related: #988713
  mentioning --rsyncable in synopsis

* Tue Jul 22 2014 jchaloup <jchaloup@redhat.com> - 6.6.2-4
- related: #1058793
  url on a new line
- related: #964160
  adding cracklib-format.8

* Fri Jul 18 2014 jchaloup <jchaloup@redhat.com> - 6.6.2-3
- related: #1003511
  .so directive rpc.idmapd.8 ~> idmapd.8

* Wed Jul 16 2014 jchaloup <jchaloup@redhat.com> - 6.6.2-2
- related: #815680
  new build

* Tue Jul 15 2014 jchaloup <jchaloup@redhat.com> - 6.6.2-1
- related: #1074599
- removed bug fixed in original component: #809096
- removed bug fixed in original component: #1011109
- removed bug fixed in original component: #1011145
- removed bug fixed in original component: #1011216
- resolves: #1108028
  ciphers.1 missing description of ECC and TLSv1.2 suites
- resolves: #1003511
  idmapd.8 man page options update
- resolves: #953741
  proc.5 /proc/fs/ not empty directory
- resolves: #964160
  cracklib-[un]packer.8 .so directive to cracklib-format.8
- resolves: #1114785
  host.conf multi on by default
- resolves: #1099335
  febootstrap-to-supermin.8 typo
- resolves: #1099275
  mailx.1 environment variables conflict
- resolves: #816252
  replacing unreadable russian mans for readable ones. For simplcity, all ru man pages replaced.
- resolves: #903666
  tar.1 reference to info tar added to description
- resolves: #1075152
  xinetd.1 xinetd reload termination handling information
- resolves: #1017478
  flock.2 nfs locks
- resolves: #818780
  oddjobd-mkhomedir.conf missing man page added
- resolves: #1007865
  updating .so directive in various snmp man pages
- resolves: #969502
  rpm --setperms and --setugids are mutually exclusive
- resolves: #889049
  vhostmd man page configuration file path correction
- resolves: #815680
  new man pages lvmcache.7 and lvmthin.7
- resolves: #1087503
  update information about codeset for charsets.7 and nl_langinfo.3
- resolves: #1112708
  bash.1 POSIX mode block size
- resolves: #891928
  man man page missing -D option added
- resolves: #781499
  makedeltarpm.8 missing attribute -l file and its description
- related: #815680
  removing added man pages for lvm2

* Mon Jun 09 2014 jchaloup <jchaloup@redhat.com> - 6.6.1-1
- resolves: #1074599
- removed bug fixed in original component: #1011219
- removed bug fixed in original component: #1023045
- removed bug fixed in original component: #1011237
- removed bug fixed in original component: #1011076
- removed bug fixed in original component: #1011064
- removed bug fixed in original component: #1011052
- removed bug fixed in original component: #882952
- removed bug fixed in original component: #1011230
- resolves: #1039986
  vsftpd.conf man page typo
- resolves: #1066537
  missing b emulate option in man pages
- resolves: #1059828
  missing pthread mutex man pages (new file in tarball)
- resolves: #1078319
  core(5) wrong default value for coredump_filter (new file in tarball)
- resolves: #1058738
  nscd.conf netgroup caching information missing
- resolves: #1058793
  curl wrong nss link
- resolves: #735949
  DESTDIR removed from man page
- resolves: #988713
  rsyncable option missing in gzip.1 man page
- resolves: #1058100
  nscd.conf default settings
- resolves: #1058349
  getgrnam.3 buffer size
- resolves: #1075233
  mention pcresyntax.3 in pcregrep.1 description

* Mon Mar 10 2014 Peter Schiffer <pschiffe@redhat.com> 6.6.0-1
- resolves: #1057712
  removed fixes for openssh package

* Thu Oct 24 2013 Peter Schiffer <pschiffe@redhat.com> 6.5.2-1
- related: #807323
  fixed typo on byzanz-record(1) man page
- related: #896700
  fixed even more missing text in auditd.conf(5) man page
- related: #913191
  fixed typo on selinux(8) man page
- resolves: #1020432
  properly documented -Z option for passing principal
  list on ssh-keygen(1) man page
- resolves: #1020417
  removed incorrect default values of KexAlgorithms on ssh_config(5) man page
- resolves: #833868
  fixed dig(1) man page
- resolves: #1018622
  updated description of "new station" message on arpwatch(8) man page

* Tue Sep 24 2013 Peter Schiffer <pschiffe@redhat.com> 6.5.1-1
- related: #996478
  mpo remove tracker
- removed bug fixed in original component: #881779
- resolves: #896700
  fixed missing text in auditd.conf(5) man page
- resolves: #1002071
  updated description of extglob behavior in bash(1) man page
- resolves: #807323
  added description of webm format to byzanz-record(1) man page
- resolves: #885625
  fixed typo on cupsctl(8) man page
- resolves: #905066
  fixed documentation regarding CA certificates in curl package
- resolves: #896544
  fixed typos in curl package man pages
- resolves: #913088
  fixed typo in security_compute_av(3) man page
- resolves: #913191
  updated selinux(8) man page
- resolves: #979460
  added clarification about setting variables on mailx(1) man page
- resolves: #960281
  documented missing values in clock_getres(2) man page
- resolves: #974697
  updated description of LD_PRELOAD variable in ld.so(8) man page
- resolves: #953753
  documented /proc/[pid]/oom_score_adj on proc(5) man page
- resolves: #953750
  documented /proc/sys/kernel/dmesg_restrict on proc(5) man page
- resolves: #953539
  documented /proc/sys/kernel/kptr_restrict on proc(5) man page
- resolves: #908295
  fixed typo on syslog(3) man page
- resolves: #974685
  removed incorrect example from sched_setaffinity(2) man page
- resolves: #988125
  documented MADV_DONTDUMP and MADV_DODUMP on madvise(2) man page
- resolves: #903258
  documented FALLOC_FL_PUNCH_HOLE flag on fallocate(2) man page
- resolves: #957010
  fixed return type of strtoul(3) and strtoull(3)
- resolves: #928917
  updated description of O_DIRECT on open(2) man page
- resolves: #979318
  described ipv6 on netstat(8) man page
- resolves: #951826
  updated default settings of inet_protocols variable on postconf(5) man page
- resolves: #872144
  backported fix for top(1) man page
- resolves: #983066
  removed deprecated example from rhnreg_ks(8) man page
- resolves: #904970
  fixed typos on rsync(1) man page
- resolves: #907837
  fixed description of -u option on useradd(8) man page
- resolves: #884699
  fixed typo in usb-devices(1) man page
- resolves: #972764
  removed superfluous dots after "via" preposition in yum man pages

* Tue Aug 13 2013 Peter Schiffer <pschiffe@redhat.com> 6.5.0-1
- resolves: #996478
  mpo remove tracker
- removed bug fixed in original component: #659661
- removed bug fixed in original component: #714079
- removed bug fixed in original component: #714084
- removed bug fixed in original component: #809550

* Thu Dec  6 2012 Peter Schiffer <pschiffe@redhat.com> 6.4.1-1
- resolves: #872526
  mentioned ext4 support in dump(8) man page
- resolves: #853959
  added missing --no-tpm option in rngd(8) man page
- resolves: #867332
  mentioned that groupmems command is not setuid in groupmems(8) man page
- resolves: #849201
  added missing alsaunmute(1) man page
- resolves: #806845
  updated dmidecode(8) man page
- resolves: #845657
  updated description of localalloc option on the numactl(8) man page
- resolves: #814417
  updated vnc documentation for -SecurityTypes option
- resolves: #846591
  added missing options to the ipmitool(1) man page

* Mon Oct 15 2012 Peter Schiffer <pschiffe@redhat.com> 6.4.0-1
- resolves: #866386
  mpo remove tracker
- removed bug fixed in original component: #676355
- removed bug fixed in original component: #714073
- removed bug fixed in original component: #714074
- removed bug fixed in original component: #714075
- removed bug fixed in original component: #714078
- removed bug fixed in original component: #729984
- removed bug fixed in original component: #735789
- removed bug fixed in original component: #745152
- removed bug fixed in original component: #745501
- removed bug fixed in original component: #745521
- removed bug fixed in original component: #745733
- removed bug fixed in original component: #799958
- removed bug fixed in original component: #809108
- removed bug fixed in original component: #809117
- removed bug fixed in original component: #809139
- removed bug fixed in original component: #809144
- removed bug fixed in original component: #809564
- removed bug fixed in original component: #820183
- removed bug fixed in original component: #690800
- renamed all patches to include bug id

* Wed May 09 2012 Peter Schiffer <pschiffe@redhat.com> 6.3.3-1
- related: #528879
  fixed name section in the unsquashfs.1 man page
- resolves: #529335
  added missing pages: fusermount.1, ulockmgr_server.1 and mount.fuse.8
- resolves: #810910
  mount(8) man page should include relatime in defaults definition

* Fri Apr 06 2012 Peter Schiffer <pschiffe@redhat.com> 6.3.2-1
- resolves: #745467
  added manual page for pkcs_slot
- resolves: #801742
  fixed redundant "works" word in request-key.conf man page
- resolves: #695363
  added description of auditing support to the iptables and ip6tables man pages
- resolves: #801784
  fixed typo in the yum man page
- resolves: #747970
  added description of -D option to the lsblk man page
- resolves: #769566
  fixed description of --group-info option in the wbinfo man page
- resolves: #766341
  removed -s option from cgcreate man page
- resolves: #801783
  added description of auditing support to the ebtables man page
- resolves: #800256
  added description of EIDRM error to the shmop man page
- resolves: #653908
  added missing options to the replcon man page
- Removed bug fixed in original component: #737990

* Tue Mar 06 2012 Peter Schiffer <pschiffe@redhat.com> 6.3.1-1
- resolves: #605521
  added manual page for urlgrabber
- resolves: #768949
  updated info about trapt in bash manual page
- resolves: #528879
  added missing pages: mksquashfs.1 and unsquashfs.1
- Removed bug fixed in original component: #659646
- Removed bug fixed in original component: #659705
- Removed bug fixed in original component: #659713
- Removed bug fixed in original component: #659720
- Removed bug fixed in original component: #674864
- Removed bug fixed in original component: #674866
- Removed bug fixed in original component: #676636
- Removed bug fixed in original component: #676643
- Removed bug fixed in original component: #714086
- Removed bug fixed in original component: #745133

* Tue Oct 18 2011 Peter Schiffer <pschiffe@redhat.com> 6.2.3-2
- related: #694860
  Rewritten patch for nsswitch.conf man page

* Thu Oct 13 2011 Peter Schiffer <pschiffe@redhat.com> 6.2.3-1
- resolves: #740670
  vsftpd: documentation for 'max_per_ip' default setting is wrong
- resolves: #717770
  Need single-request-reopen option documented for resolv.conf
- resolves: #742098
  Update description of timeo in nfs(5) manpage
- resolves: #694860
  No mention of sssd in nsswitch.conf man page
- resolves: #723791
  Lack of UMOUNT_NOFOLLOW flag description in umount(2)
- resolves: #728416
  [RFE] net: backport sendmmsg syscall [Manpage request]

* Wed Sep 14 2011 Peter Schiffer <pschiffe@redhat.com> 6.2.2-1
- resolves: #727526
  Typo in man curl manpage
- resolves: #730042
  Add missing man page for cpufreq-aperf and fixed cpufreq-set man page
- resolves: #602228
  bridge-utils missing documentation in manpage for RFE 574461
- resolves: #731690
  Man ecryptfs contains invalid link in SEE ALSO section
- resolves: #734836
  Document that realtime clock functions need to link with -lrt
- resolves: #656245
  Fixed incorrect link from previous release
- resolves: #690187
  Added license file for man pages from man-pages package
  Removed bug fixed in original component: #659740
  Added license file for man page from x86info package

* Fri Jul 8 2011 Ivana Hutarova Varekova <varekova@redhat.com> 6.2.1-1
- resolves: #698151
  Remove documentation for "order" keyword in /etc/host.conf manpage
- resolves: #688543
  Several lsvpd tools options not documented in man page
- resolves: #674423
  man page for recvmmsg added
- resolves: #656245
  add fattach.2 link to uninplemented
- resolves: #719902
  Remove bug fixed in original component: #674870
  Remove bug fixed in original component: #674878
  Remove bug fixed in original component: #677541
  Remove bug fixed in original component: #677542
  Remove bug fixed in original component: #690801
  Remove bug fixed in original component: #674883

* Fri Jul 8 2011 Ivana Hutarova Varekova <varekova@redhat.com> 6.2.0-1
- resolves: #712256
  Typo in volume_key manpage
- resolves: #709274
  ntpq(8) manpage fixes
- resolves: #709058
  ntp-keygen(8) manpage fixes
- resolves: #615897
  Added missing man page for/usr/sbin/lsmsr in x86info package
- resolves: #690187
  New man pages for cciss + hpsa modules

* Wed Apr 13 2011 Ivana Hutarova Varekova <varekova@redhat.com> 2.5-1
- related: #676483
  remove the man pages, they are already fixed in nss-pam-ldap package

* Tue Apr 12 2011 Ivana Hutarova Varekova <varekova@redhat.com> 2.4-1
- related: #604626
  add forgotten patch
- related: #632081
  fix the encoding
- related: #644308
  fix the typo
- related: #650162
  fix the patch text
- related: #676483

* Thu Mar 31 2011 Ivana Hutarova Varekova <varekova@redhat.com> 2.3-1
- resolves: #676483
  nss-pam-ldapd: troff syntax error in the man page of nslcd

* Fri Mar 25 2011 Ivana Hutarova Varekova <varekova@redhat.com> 2.2-1
- resolves: #675223
  locate(1) manpage fixes
- resolves: #676540
  magic(5) manpage fixes

* Thu Feb 10 2011 Ivana Hutarova Varekova <varekova@redhat.com> 2.1-1
- resolves: #615873
  Man w3m is stating incorrect program version (package w3m)
- resolves: #675213
  userpasswd(1) manpage fix (package usermode)
- resolves: #675688
  pcretest(1) manpage fixes (package pcre)
- resolves: #675682
  pcregrep(1) manpage fixes (package pcre)
- resolves: #636785
  "semanage module" is not mentioned in semanage man page (package policycoreutils)
- resolves: #540492
  8 options are not described in semanage man page (package policycoreutils)

* Tue Feb  8 2011 Ivana Hutarova Varekova <varekova@redhat.com> 2.0-1
- resolves: #658734
  setacl(1) man page bug (package acl)
- resolves: #651120
  setfattr(1) man page bug (package attr)
- resolves: #615905
  ospfclient(8) and watchquagga(8) man pages added (package quagga)
- resolves: #633701
  expect(1) man page is bad formatted (package expect)
- resolves: #650162
  useradd(8) man page bug (package shadow-utils)
- resolves: #657563
  Manual page corrections for find(1) (package findutils)
- resolves: #632081
  man(1) for Japanese manual page contains duplicated lines in PAGER explanation
  (package man)
- resolves: #604626
  yum-verify man page uses 'pretty' quotes in examples (package yum-utils)
- resolves: #622451
  Author info is wrong in man page (package logrotate)
- resolves: #638625
  Ambiguity in logrotate man page (package logrotate)
- resolves: #644308
  manpage not in sync with options logrotate actually recognizes (package logrotate)
- resolves: #613979
  dftest and randpkt does not have a man page (package wireshark)
- resolves: #619779
  lftp(1) option xfer:auto-rename not documented (package lftp)
- resolves: #673968
  logrotate(8) manpage typo patch (package logrotate)

* Mon Oct 19 2009 Ivana Varekova <varekova@redhat.com> 1.0-1
- made a initial package
