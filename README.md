# 2D Game Programming Term Project

##Title: Guilty and Rain
---
### 게임 소개
만드려고 하는 작품으로 모방할 게임은 **ENDER LILES: Quietus of the Knights**이며,
장르는 **메트로배니아 장르의 액션 RPG**다.

![ENDER LILIES 스크린 샷](https://github.com/user-attachments/assets/00237f02-fb62-471e-b416-3c883a1a06db)

[ENDER LILES: Quietus of the Knights 플레이 영상](https://youtu.be/4IAgZRLtg-Q?si=yXSfOJwddHiKzfuY)

메트로배니아 장르의 게임들처럼 **여러 개의 작은 맵**들이 유기적으로 **연결**되어 **하나의 큰 맵**을 만들고, 이 **맵을 탐색**하는 게임이다.
플레이어는 각 맵마다 존재하는 적들을 물리쳐야 다음 맵으로 이동할 수 있다.
(이 설명에서는 큰 맵을 **'월드'**, 작은 맵을 **'스테이지'** 로 정의함.)

![map](https://github.com/user-attachments/assets/aebdd865-060d-4776-9723-7ad9571c2042)

**게임 초반에 갈 수 없을 것 같은 장소**는 게임을 진행하면서 얻을 수 있는 **새로운 능력**을 얻고 나면 갈 수 있게 된다. 
이 새로운 능력은 탐색 뿐 아니라 **전투**에도 영향을 끼칠 수 있는 능력이다.

모든 스테이지를 탐색하는 것이 필수는 아니지만 탐색을 통해 여러 아이템을 얻을 수 있다.
클리어 조건은 여러 스테이지를 탐색을 하면서 **보스방이 나오는 스테이지를 찾고, 보스방에서 나오는 보스를 물리치면 게임을 클리어한다.**

세계관은 대략적으로 중세 판타지(ENDER LILES와 같은 느낌으로 생각하고 있으면 된다.)로 꾸려나갈 예정. 

**조작 방법**은 **키보드**와 **마우스**를 이용한다.
기본적으로 **마우스 좌클릭 - 공격(주인공은 검을 사용하는 캐릭터), wasd - 이동, space - 점프, shift - 회피** 등이 있으며, 
새로운 능력을 얻을 때마다 그에 해당하는 해당 조작 키를 알려준다.

다른 게임과 차별을 두려는 요소는 연출로 나오는 타격감이다.
이에 관련해서는 아래에서 스케치 그림과 함께 간단하게 설명.

---
### 예상 게임 실행 흐름
---
![전체적인 맵 구성(예)](https://github.com/user-attachments/assets/f0dd1005-5a1f-4c86-a9cd-db99ac1219c3)
---
월드 구성을 예로 들면 이렇게 생겼다. 그림의 위 쪽은 월드, 아래 쪽은 스테이지의 생김새이다. 

플레이어는 스테이지들을 탐색하면서 새로운 능력을 얻고, 보스방을 깨면 다음 스테이지로도 넘어갈 수 있다.
월드의 구조에 따라 스테이지에서 다른 스테이지로 이동할 때의 입구 위치가 조정되어있다.

---
![UI와 더블 점프 활용](https://github.com/user-attachments/assets/fd4ce426-aea3-4a72-bb6e-dd10e9dd1105)
---
이 그림은 UI의 구성과 메트로배니아 방식의 게임 진행 중 한가지를 보여준다. 
UI의 구성은 대략 이렇다. 왼쪽 상단에는 레벨, HP와 같은 자원을 표시하고, 왼쪽 하단에는 스킬 UI가 있다. 스킬 UI는 쿨타임을 보는 용도로 사용.
오른쪽 상단에는 월드의 구조를 보여주는 미니맵이 있는데, 키를 통해 열거나 닫을 수 있다.

메트로배니아 방식의 게임 진행 중 게임 초반에 갈 수 없을 것 같은 장소는 게임을 진행하면서 얻을 수 있는 새로운 능력을 얻고 나면 갈 수 있게 된다.
즉, 검은색 화살표를 진행하고 있는 플레이어는 더블 점프 능력이 없어 높은 위치의 스테이지를 갈 수 없지만, 빨간색 화살표 진행 방향으로 진행하면서
더블 점프 능력을 얻으면 파란색 화살표처럼 높은 위치의 스테이지로 이동할 수 있다.

---
![슈퍼 회피, 작살 클러치](https://github.com/user-attachments/assets/ff70fd33-5985-4970-9159-efe8ed3c71ad)
---
이 그림은 타격감과 관련된 연출을 보여주기 위해 자주 사용되는 새로운 능력 2가지를 보여준다. 1번은 슈퍼 회피, 2번과 3번은 작살 클러치다.

슈퍼 회피는 적이 공격할 타이밍에 회피를 하면 자동으로 발동된다.
슈퍼 회피가 발동되면, 시간이 느려지는 연출과 함께 다음 공격은 치명타로 발동된다.

작살 클러치는 휠 클릭으로 작살을 발사하고, 좌클릭 또는 우클릭을 누르면 사용할 수 있고, 휠 클릭을 다시 누르면 해제가 가능하다.
좌클릭은 플레이어가 움직이고, 우클릭은 오브젝트가 당겨진다. 우클릭의 경우에는 각 오브젝트마다 차이점이 있으므로, 아래 오브젝트 상호작용에서 다룸.

능력을 사용하는 과정에서 타격감을 살리는 연출(개발 내용 참고)을 더 추가해준다.
그 외 추가적인 연출은 아래 개발 내용 부분에서 다룰 예정.

---
### 개발할 내용(나중에 추가가 필요한 부분은 *)(1차 발표 전 활동)
---
#### 1. Scene의 종류 및 구성, 전환 규칙(*)
---
+ 타이틀 화면
---
![타이틀 화면](https://github.com/user-attachments/assets/93e14b74-a5f8-4eb6-8eee-92b9023cab39)
---
+ 스테이지(예상 게임 실행 흐름 사진 참고)
	1. 게임 클리어
		+ 보스 격파 시
		
  ![게임 클리어](https://github.com/user-attachments/assets/24af5dff-5d84-4596-a044-7628f324b89b)

	2. 게임 오버
		+ HP가 0이 될 시
		
  ![게임 오버](https://github.com/user-attachments/assets/673b546b-4a85-411f-ab79-db0208006502)

	3. 일시정지 메뉴(인벤토리, 스킬 관리, 옵션 등)
		+ 메뉴 키를 눌렀을 때
		![menu](https://github.com/user-attachments/assets/f995e179-734d-42ac-be48-7adb15941c0b)

	4. 다른 스테이지
		+ 다른 스테이지 이동 장소로 이동했을 때
---
#### 2. 각 Scene에 등장하는 GameObject의 종류 및 구성, 상호작용
---
![플레이어](https://github.com/user-attachments/assets/0689fe7a-0b54-41b2-8b01-d718904fb3ea)
##### 플레이어(Player)
+ 무기(Weapon)
	+ 검(Sword)
	+ 작살 클러치(Harpoon Clutch)

+ 스킬(Skill)(*)
	+ 더블 점프(Double Jump)
	+ 슈퍼 회피(Super Step)
	+ 올려베기(Upper Slash)

+ 체력(HP)
+ 공격력(Atk)
+ 레벨(Level)
+ 경험치 자원(Exp)
+ 골드 자원(Gold)

+ 위치(position)
	+ x 좌표
	+ y 좌표
	+ 크기(scale)
	+ 움직임(move)
 
+ 아이템(Item)(*)
	+ 포션(Potion)
---
![몬스터](https://github.com/user-attachments/assets/3b8a5cc8-1181-4333-bd53-3fb890d5bc80)
##### 몬스터(Monster)
+ 체력(HP)
+ 공격력(Atk)
+ 레벨(Level)
+ 골드 드랍(Gold)
+ 경험치 드랍(EXP)

+ 위치(position)
	+ x 좌표(x)
	+ y 좌표(y)
	+ 크기(scale)
	+ 움직임(move)

+ 종류(type)
	+ 일반 몬스터(Normal Monster)(*)
	+ 보스(BOSS)(*)
---
##### 스테이지(Stage)
+ 상호작용이 가능한 지형 지물 또는 구조물(각각 위치(position) 추가)
	+ 구조물(Structure)
		+ 벽과 바닥(wall and floor)		
		+ 가시(danger)
		+ ![가시](https://github.com/user-attachments/assets/aafb46e0-739c-4143-84f4-cded163b0c68)
		+ 나무상자(box)
	+ 스킬 획득(Skill Acquire)
		+ ![스킬 획득](https://github.com/user-attachments/assets/fc11342d-094a-4936-b274-d72ff14ad058)
	+ 다음 스테이지 이동 장소(next stage)
---
##### 각종 상호작용(Interaction)
+ 플레이어와 몬스터
	+ 공격
	+ 피격
	+ 경험치
	+ 돈
	+ 스킬
+ 플레이어와 지형 지물
	+ 벽과 바닥 충돌(몬스터)
	+ 스킬
	+ 스킬 획득 충돌
	+ 가시 충돌 의한 피격
	+ 박스(고정 x)
	+ 다음 스테이지 이동 장소 충돌
---
#### 3. 사용한/사용할 개발 기법들에 대한 간단한 소개
---
+ 패럴랙스 스크롤링(Parallax Scrolling)
	+ 시차 스크롤링(parallax scrolling, 패럴랙스 스크롤링)은 사용자가 마우스를 스크롤할 때, 원거리에 있는 배경 이미지는 느리게 움직이게 하고, 근거리에 있는 사물 이미지는 빠르게 움직이도록 함으로써 입체감을 느낄 수 있게 만든 디자인 기법이다. 
	+ 하나의 이미지를 여러 개의 레이어(layer)로 분리한 후 스크롤에 반응하는 속도를 다르게 조정하는 방식으로 구현한다.
+ 더블 버퍼링(Double Buffering)
	+ 주로 컴퓨터 그래픽에서 사용되는 용어로서 비디오 메모리만을 사용한 싱글 버퍼링으로 그래픽을 그릴 경우 데이터를 저장하는 동안에는 다음 그림의 데이터를 전송할 수 없기 때문에 지우고 그리고 지우고 그리고 할 경우 필연적으로 발생하는 깜빡임, 찢어짐 등의 상황을 막기 위해서 사용되는 기법이다.
	+ 더블 버퍼링을 통해 Animation을 효과적으로 그린다.
+ 행동 트리(Behavior Tree)
	+ 주로 게임 AI나 로봇 제어에서 사용되는 계층적 모델로, 특정 목표를 수행하기 위해 다양한 행동을 순차적 또는 병렬적으로 실행하는 구조다.
	+ 몬스터의 인공지능 구현을 위해 사용	

+ GFW
	+ 출력
	+ 키 입력
	+ 애니메이션(time)
	+ Scene(stack)
	+ 게임 월드
	+ 충돌 감지
	+ 게임 인공지능
	+ 파일 입출력
	+ 맵 에디터
---
### 개발 진행 상황
---
+ 1주차: GFW 구현 완료, 플레이어와 몬스터 객체 속성 추가와 생성, 상호작용 추가 - 100% 완료
	
+ 2주차: 계획대로 스테이지 객체를 만들고 10개의 스테이지를 생성해서 플레이어와 몬스터의 위치를 정함 - 100% 완료

	+ 대략적인 스테이지를 구성

	![대략적인 스테이지 구성](https://github.com/user-attachments/assets/35b14f86-8d95-4e42-9e2d-0e2100a8ce36)
	
	+ Scene 다이어그램
	+ Stage를 Scene으로 관리하지 않음.

	![Scene 다이어그램](https://github.com/user-attachments/assets/c77893d1-c391-4151-9a4f-3d32209e4e35)
	
	+ 타이틀 화면에서 Load를 할 지, New Game을 할 지 선택 가능

	![타이틀 화면](https://github.com/user-attachments/assets/2fd54d9f-6834-4ec2-87c1-2db0acbe9f21)
	
	+ 10개의 스테이지 구성 후 스테이지 생성 완료

+ 3주차: 일시정지 메뉴 구현 x - 90% 완료
	+ 배경 Scroll 가능(패럴랙스 스크롤링)
	+ Title Scene 구현
	+ 스테이지 구성은 전부 완료, 아이템만 추가하면 됨.

+ 4주차: UI 구현 부족 - 80% 완료
	+ 몬스터 인공지능 구현 완료
	+ 보스 구현 완료
	+ 이미지, 사운드 추가

![insights](https://github.com/user-attachments/assets/cded8dd4-58af-4316-9ec7-5a3fd442b02b)

![주차별 커밋 수](https://github.com/user-attachments/assets/0be86f5d-7e35-479e-af0c-fa1efb6845fb)

---
### 아쉬운 점
---

+ 하고 싶었지만 못한 것
	+ 애니메이션
    	+ 달리기 공격
    	+ 콤보 공격
    	+ 공격의 fps
    	+ 공격의 범위와 sprite 범위 재설정
    	+ 스킬 구현(클러치, 슈퍼회피)
	+ 그 외 스테이지, 몬스터 종류, 아이템 추가 등

+ 팔기 위해 보충할 것들
	+ 컨텐츠 추가, 스토리 추가, 리소스 추가

+ 해결하지 못한 버그
	+ 충돌처리 문제. 좌우, 상하 충돌이 중복될 때 문제가 생김.

+ 기말 프로젝트를 하면서 겪은 어려움
	+ 코드의 양이 늘어나면 늘어날수록 오류가 생겼을 때 문제를 찾고, 해결하는 데에 어려움을 겪었다.

+ 수업에 대한 내용
	+ 이번 수업에서 기대한 것
		+ GFW를 구현하여 게임 프로그래밍을 좀 더 간편하게 관리하고, 쉽게 프로그래밍하는 법
		+ 기획한 것을 어떤 방법으로 어떻게 구현하는 지

	+ 이번 수업에서 얻은 것
		+ GFW의 기본 틀, 확실하게 관리가 편하고, 프로그래밍이 간단했다.
		+ 기획 방법에 대해서 다시 고민할 수 있었다.
		+ 여러 게임 로직의 구현 방법을 알 수 있었다.

---
### Main Game Scene에 나오는 Game Object
---
+ 메인 씬이 시작하면 Stage와 플레이어 객체를 생성한다.

+ Stage
	+ Stage 클래스는 인덱스를 받고, 그 인덱스에 맞는 스테이지를 Tiled로 만든 tmx 파일을 이용해 맵을 만든다.
	+ tmx 파일에 포함되어 있는 오브젝트들은 floor 클래스와 monster 클래스다. 추가적으로 스킬 아이템도 생성한다.
	+ 각 스테이지에 스테이지 전환 트리거를 넣어 플레이어가 스테이지 내의 몬스터를 모두 물리친 후 트리거의 위치에 가게 되면 스테이지가 전환된다.
	+ 추가적으로 Stage가 전환될 때마다 자동저장(save, load)을 한다.

+ Player
	+ Player 클래스는 a와 d키로 기본적인 움직임, space로 jump가 가능하다.
	+ state에 따라서 애니메이션이 달라진다.
	+ Attack이란 클래스로 몬스터를 공격할 수 있다. 공격은 좌클릭으로 좌클릭을 할 때마다 PlayerAttack 클래스를 생성.
	+ 몬스터를 잡게 되면 몬스터로부터 재화를 받을 수 있다.
	+ 일정 경험치를 얻게 되면 레벨 업을 하고 SP를 얻는다. SP는 능력치를 올릴 수 있는데 사용한다.(SP 관련 시스템 구현 X)

	+ 스킬(doublejump를 제외한 모든 스킬은 쿨타임이 존재한다.)
		+ doublejump
			+ 점프를 두 번 할 수 있다.
		
		+ roll
			+ shift를 눌러 몬스터의 공격을 회피할 수 있다. 시전동안에는 무적이지만 다른 행동을 할 수 없다.

		+ upperslash
			+ 우클릭을 통해 강력한 데미지를 주는 공격이다.

	+ 스킬 아이템을 통해서 획득 가능하다.

+ Monster
	+ Hp가 0이 되면 객체가 삭제되며, 플레이어에게 재화를 준다.
	+ 기본적으로 대기하며, 시간이 지나면 x축으로 한 번 이동한다.
	+ 플레이어의 위치가 어느정도 가까워지면 플레이어를 추격한다.
	+ 플레이어의 위치가 공격 가능한 위치라면 공격을 한다.
	+ 공격을 할 때는 모든 행동을 멈춘다.
	+ 한 번 공격에는 시간이 걸린다.
	+ 보스는 일반 몬스터보다 강력하다. 보스를 잡으면 게임을 클리어한다.

+ Floor
	+ Monster와 Player의 객체와 충돌이 일어나면(world.collides box) floor의 각 tild_id에 따라서 충돌이 달라진다.
	+ 옆면 충돌처리까지 구현완료.
	+ player.cx에 따라 스크롤링이 되고 있다. player가 화면의 중앙에 있을 때 player.x가 아닌 player.cx를 움직이게 한다.

---
### 일정
---
#### 1. 준비 사항
---
+ 대략적인 스테이지 구성
	+ 맵 에디터를 배운 후 먼저 그림판으로 그려 볼 예정 (11/6)
	+ Scene 상태 다이어그램도 같이 그릴 예정(11/6)

---
#### 2. 세부 일정
---
+ 기간: 10/29(화) ~ 11/26(화)
	+ 1주차: GFW 구현 후 플레이어와 몬스터 생성
		+ 11/2(토) - GFW 구현, 플레이어, 몬스터 그리면서 pico2D에 적응, 객체 속성 추가, 상호작용(스킬 제외).
	
	+ 2주차: 스테이지 구성
		+ 11/6(수) - 대략적인 스테이지 구성, 스테이지 객체 선언
		+ 11/9(토) - 맵 에디터로 스테이지 구성 후 스테이지 생성(플레이어, 몬스터 x)
	
	+ 3주차: 스테이지 구성 완성 후 Scene 구성 및 전환
		+ 11/13(수) - 플레이어 스킬 구현 및 몬스터와 스테이지 상호작용
		+ 11/16(토) - 스테이지에 플레이어와 몬스터 생성. 아이템 구현, Scene 구성 및 전환.

	+ 4주차 : Save, Load, 몬스터 인공지능, 이미지, 사운드 구현
		+ 11/20(수) - 저장, 불러오기 구현, 전투 연출.
		+ 11/23(토) - 몬스터의 종류, 인공지능, BOSS 구현. 리소스 구해서 이미지, 사운드 구현.
		+ 11/24(일) - 2차 발표 전 점검 및 발표 준비

+ 기간: 11/26(화) ~ 12/13(금)
	+ 11/27(수) - 아이템, 스테이지, 스킬, 몬스터 종류 추가
	+ 11/30(토) - 보완, 추가 및 유지보수
	+ 12/4(수) - 보완, 추가 및 유지보수
	+ 12/12(목) - 마지막 점검 및 발표 준비
---
### Youtube Link
---
+ 1차 발표: [1차 발표 영상](https://youtu.be/jYb6tdUZK7g?si=7oV2OZMaJpzY8354)
+ 2차 발표: [2차 발표 영상](https://www.youtube.com/watch?v=WKfDIfGfr0M)
+ 3차 발표: [최종 발표 영상](https://youtu.be/lecw62rz4nQ?si=YU7ZYgMew-vM5Onj)
